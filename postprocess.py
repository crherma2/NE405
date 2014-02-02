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

set xlabel '{xlabel}'
set ylabel '{ylabel}'

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
    def __init__(self, x, xlabel, y, ylabel):
        self.x=x
        self.xlabel = xlabel
        self.y=y
        self.ylabel = ylabel
    def write_gnuplot(self, outfile):

       data_str = ''
       for i in range(len(self.x)):
           data_str += '{x} {y}\n'.format(x = self.x[i], y = self.y[i])
       file_str = plot_template.format(outfile=outfile, data=data_str,
                                       xlabel=self.xlabel, ylabel=self.ylabel)

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
        name_dict.update({keyns:name_dict.pop(key)}) # change key in name dictionary to no spaces

    # looping through lines
    i = 0
    while i<len(lines):

        # first line create data objects
        if i==0:
            sline=lines[i].split()
            idx = 0
            for key in sline:              
                data_dict.update({key:Data(name_dict[key],idx)})
                idx +=1
            i +=1
            continue

        # for all other lines append data points
        sline=lines[i].split()
        for key in data_dict.keys():
            data_dict[key].add_datapt(sline[data_dict[key].idx])
            
        i +=1 # next line
    
    # create plot objects
    for key in data_dict.keys():
        if key == 'time':
            continue
        
        x = data_dict['time'].pts
        xlabel = data_dict['time'].name
        y = data_dict[key].pts
        ylabel = data_dict[key].name
        plot_dict.update({key:Plot(x, xlabel, y, ylabel)})
    
    # run plots
    for key in plot_dict.keys():
        plot_dict[key].write_gnuplot(key)

if __name__ == '__main__':
    filename=sys.argv[1]
    main(filename)
