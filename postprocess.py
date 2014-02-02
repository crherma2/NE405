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

class Plot(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y


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
                idx +=1
            i +=1
            continue


        # for all other lines append data points
        sline=lines[i].split()
        for key in data_dict.keys():
            print key
            data_dict[key].add_datapt(sline[data_dict[key].idx])
            

        i +=1
    
    # create plot objects
    for key in data_dict.keys():
        if key == 'time':
            continue
        
        x = data_dict['time'].pts
        y = data_dict[key].pts
        plot_dict.update({key:Plot(x,y)})
    
    print plot_dict["Pp"].y


if __name__ == '__main__':
    filename=sys.argv[1]
    main(filename)
