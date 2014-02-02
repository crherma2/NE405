#!/usr/bin/env python2

from collections import OrderedDict
import sys

data_dict=OrderedDict()
plot_dict=OrderedDict()


class Data(object):
    def __init__(self, name):
        self.name=name
        self.pts=[]

    def add_datapt(self, pt):
        self.pts.append(pt)


def main(filename):

    # read in file
    with open(filename,'r') as fh:
        lines=fh.read().splitlines()

    print lines

if __name__ == '__main__':
    filename=sys.argv[1]
    main(filename)
