#!/usr/bin/python2
#
# Plot a three-dimensional histogram of activation
# Copyright (C) 2014-2015 Tim Cooijmans (CERN PH/CMX BRIL, Maastricht University) <cooijmans.tim@gmail.com>
#
# This file is part of Sesame.
#
# Sesame is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Sesame is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import numpy as np
import matplotlib.pyplot as plt
import subprocess as sp
import logging as log
import tempfile
import os
import functools as ft
import re
import argparse

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
HISTOGRAM_PATH = os.path.join(SCRIPT_DIRECTORY, "src", "histogram")

class Binning(object):
    regex = re.compile(r"^(?P<a>{0}):(?P<b>{0})/(?P<k>\d+)$"
                       .format(r"[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?"))

    def __init__(self, a, b, k):
        self.a = a
        self.b = b
        self.k = k

    @classmethod
    def parse(klass, s):
        match = klass.regex.match(s)
        if not match:
            raise ValueError("invalid binning specification: '%s'" % s)
        return Binning(*tuple(parser(match.group(key))
                              for key, parser in zip("abk", (float, float, int))))

    def format(self):
        return "%f:%f/%i" % (self.a, self.b, self.k)

class Histogram(object):
    def __init__(self, binnings):
        for key in "abk":
            setattr(self, key, np.array(list(getattr(binning, key) for binning in binnings)))
        self.bins = np.zeros(self.k)

    @property
    def binnings(self):
        return tuple(Binning(a, b, k) for a, b, k in zip(self.a, self.b, self.k))

    @property
    def origin(self):
        return (self.k * (0 - self.a) / (self.b - self.a)).round().astype(np.int)

    def populate_from_resnuc_file(self, path):
        input_file = open(path, "r")
        output_file, output_path = tempfile.mkstemp()
        try:
            sp.call([HISTOGRAM_PATH,] +
                    [binning.format() for binning in self.binnings],
                    stdin=input_file, stdout=output_file)
            os.close(output_file)
            bins = np.fromfile(output_path, dtype=np.uint64)
        finally:
            os.remove(output_path)
            input_file.close()
        self.bins = bins.reshape(self.k)

    def position(self, index, dim=None):
        x = self.a + (self.b - self.a) * index / self.k
        return x[dim] if dim is not None else x

    def positions(self, indices, dim=None):
        return [self.position(index, dim) for index in indices]

class State(object):
    def __init__(self, histogram):
        self._histogram = histogram
        self.orientation = np.arange(self._histogram.bins.ndim)
        self._index = self._histogram.origin[self.orientation[0]]
        self._logarithmic = False

    @property
    def histogram(self):
        x = (np.transpose(self._histogram.bins, axes=self.orientation)
             [self.index, :, :].squeeze())
        if self._logarithmic:
            # NOTE: add 1 to avoid singularity at 0
            x = np.log(1 + x)
        return x

    @property
    def meshgrid(self):
        xs = [[], []]
        for i in (0, 1):
            dim = self.orientation[i+1]
            indices = xrange(self._histogram.k[dim] + 1)
            xs[i] = self._histogram.positions(indices, dim)
        return np.meshgrid(*reversed(xs))

    def set_rejection(self, rejection):
        # bring rejected axis to front of orientation
        self.orientation = np.hstack(
            (self.orientation[self.orientation == rejection],
             self.orientation[self.orientation != rejection]))
        self.index = self._histogram.origin[self.orientation[0]]

    def transpose(self):
        # swap displayed axes
        # NOTE: assumption of three dimensions
        self.orientation = self.orientation[np.array([0, 2, 1])]

    def toggle_logarithmic(self):
        self._logarithmic = not self._logarithmic

    # move along rejected axis
    def forward(self, dx):
        self.index += dx

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, index):
        self._index = np.clip(index, 0, self._histogram.k[self.orientation[0]] - 1)

    @property
    def position(self):
        index = np.array([self.index,] * self._histogram.bins.ndim)
        return self._histogram.position(index)[self.orientation[0]]

class GUI(object):
    def __init__(self, histogram):
        self.state = State(histogram)
        self.figure = plt.figure()
        self.figure.canvas.mpl_connect("scroll_event", self.on_scroll)
        self.figure.canvas.mpl_connect("key_press_event", self.on_key_press)

    def redraw(self):
        self.figure.clear()
        i, j = self.state.meshgrid
        plt.pcolormesh(i, j, self.state.histogram, figure=self.figure)
        axes = "x y z".split()
        plt.xlabel(axes[self.state.orientation[2]])
        plt.ylabel(axes[self.state.orientation[1]])
        plt.title("%s = %f" % (axes[self.state.orientation[0]], self.state.position))
        plt.draw()

    def on_key_press(self, event):
        handlers = dict(x=ft.partial(self.state.set_rejection, 0),
                        y=ft.partial(self.state.set_rejection, 1),
                        z=ft.partial(self.state.set_rejection, 2),
                        t=self.state.transpose,
                        l=self.state.toggle_logarithmic,
                        n=ft.partial(self.state.forward, -1),
                        m=ft.partial(self.state.forward, 1))
        try:
            handler = handlers[event.key]
        except KeyError:
            return
        handler()
        self.redraw()

    def on_scroll(self, event):
        self.state.forward(event.step)
        self.redraw()

    def show(self):
        self.redraw()
        plt.show()

ap = argparse.ArgumentParser(description="Show an interactive histogram plot of"
                             " the nuclides in the given file.")
ap.add_argument("resnucpath", metavar="FILE",
                help="the file to read nuclides from")
ap.add_argument("binnings", nargs=3, type=Binning.parse, metavar="A:B/K",
                help="the range (A to B) and number K of bins (specified once for each of x, y, z)")

if __name__ == "__main__":
    args = ap.parse_args()
    histogram = Histogram(args.binnings)
    histogram.populate_from_resnuc_file(args.resnucpath)
    gui = GUI(histogram)
    gui.show()




path = '//rpclustersrv1/cluster_temp/cbjorkma/OpeningScenarios/PROMPT/2018-10-10_10h50m03s_ATLAS_Fluences_Daniel4'


os.chdir(path)

filename = 'ATLAS_Fluences_Daniel4_116001_tsresnuc_prompt.bin'



input = open(filename, "r").readlines()

a = input_file[0:1000]

with open(filename) as f:
    for line in f.readlines():
        print line
        
        
        
        
        
        
        
        
        
        
        
        
        


