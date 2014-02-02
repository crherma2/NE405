#!/usr/bin/env python2

from collections import OrderedDict
import sys

data_dict=OrderedDict()
plot_dict=OrderedDict()


class Data(object):
    def __init__(self, name, idx):
        self.name=name
        self.idx=idx
        self.pts=[]

    def add_datapt(self, pt):
        self.pts.append(pt)


def main(filename):

    # read in file
    with open(filename,'r') as fh:
        lines=fh.read().splitlines()

    # looping through lines
    i = 0
    while i<len(lines):

        # first line create data objects
        if i==0:
            sline=lines[i].split()
            idx = 0
            for key in sline:              
                data_dict.update({key:Data(key,idx)})
            i +=1
            continue


        # for all other lines append data points
        sline=lines[i].split()
        for key in data_dict.keys():
            data_dict[key].add_datapt(sline[data_dict[key].idx])


        i +=1

    print data_dict['time'].name
    print data_dict['time'].idx
    print data_dict['time'].pts


if __name__ == '__main__':
    filename=sys.argv[1]
    main(filename)
