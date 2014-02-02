#!/usr/bin/env python2

from collections import OrderedDict
from subprocess import call
import sys

name_dict={}
data_dict=OrderedDict()
plot_dict=OrderedDict()

plot_template="""#!/bin/sh/env gnuplot

set terminal pdf enhanced
set output '{outfile}.pdf'

unset key

plot '-' using 1:2 with lines lw 4.0
{data}
"""

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
    def write_gnuplot(self, outfile):

       data_str = ''
       for i in range(len(self.x)):
           data_str += '{x} {y}\n'.format(x = self.x[i], y = self.y[i])
       file_str = plot_template.format(outfile=outfile, data=data_str)

       with open(outfile+'.plot','w') as fh:
           fh.write(file_str)

       call(['gnuplot',outfile+'.plot'])

def main(filename):

    # load in names file
    with open('names.txt','r') as fh:
        namelines = fh.read().splitlines()
    for nameline in namelines:
        sline = nameline.split(':')
        name_dict.update({sline[0]:sline[1]})

    # read in file
    with open(filename,'r') as fh:
        lines=fh.read().splitlines()

    # correct keywords in header
    for key in name_dict.keys():
        keyns = key.replace(' ','')
        lines[0] = lines[0].replace(key, keyns)

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
            data_dict[key].add_datapt(sline[data_dict[key].idx])
            

        i +=1
    
    # create plot objects
    for key in data_dict.keys():
        if key == 'time':
            continue
        
        x = data_dict['time'].pts
        y = data_dict[key].pts
        plot_dict.update({key:Plot(x,y)})
    
    # run plots
    for key in plot_dict.keys():
        plot_dict[key].write_gnuplot(key)

if __name__ == '__main__':
    filename=sys.argv[1]
    main(filename)
