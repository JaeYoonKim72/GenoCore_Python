#!/bin/env python
#Genocore python version 1.0 (made by JaeYoon Kim)
#This is a python version coverted from the orignial R version made by Seongmun Jeong 
#2019-06-01

import os, sys, collections, time, copy
import itertools
import numpy as np
import optparse
from Geno_Convert import *
from genocore import *

def parse_my_command_line():
    opt_parser = {}
    opt_parser['VCFtoCSV'] = optparse.OptionParser()
    opt_parser['CoreSet']  = optparse.OptionParser()
    opt_parser['SelectVCF'] = optparse.OptionParser()

    # VCFtoCSV
    opt_parser['VCFtoCSV'].usage = "python run_genocore.py VCFtoCSV -i [VCF file] -o [Output name] -p [Y or N (phased)] -g [Y or N (gziped)]\n    Help: python run_genocore.py VCFtoCSV -h"
    opt_parser['VCFtoCSV'].add_option('-i', '--input', default = None, type = 'str', dest='input', action='store',
        help = 'Input vcf file')
    opt_parser['VCFtoCSV'].add_option('-o', '--output', default = "testVCFtoCSV.csv", type = 'str', dest='output', action='store',  help = 'Output_name.csv')
    opt_parser['VCFtoCSV'].add_option('-p', '--pased', default = 'N', type = 'str', dest='phased', action='store',
        help = 'Wheter the VCf is phased. Select "Y" or "N" (default:"N")')
    opt_parser['VCFtoCSV'].add_option('-g', '--gziped', default = 'N', type = 'str', dest='gziped', action='store',
        help = 'Wheter the VCf is gziped. Select "Y" or "N" (default:"N")')

    # GenoCore
    opt_parser['CoreSet'].usage = "python run_genocore.py CoreSet -i [CSV file] -p [Preset txt] -c [Coverage rate] -d [Covergence rate], -o [Output name], -m [MAF rate] \n    Help: python run_genocore.py CoreSet -h"
    opt_parser['CoreSet'].add_option('-i', '--input', default = None, type = 'str', dest='input', action='store',
        help = 'Input csv file')
    opt_parser['CoreSet'].add_option('-p', '--predefined', default = None, type = 'str', dest='preset', action='store',
        help = 'Preset text file (one sample per line), This is an optional argument and can be omitted if there is no Preset')
    opt_parser['CoreSet'].add_option('-c', '--coverage', default = 99, type = 'float', dest='coverage', action='store',
        help = 'Coverage rate of selected core samples (default: 99)')
    opt_parser['CoreSet'].add_option('-d', '--delta', default = 0.001, type = 'float', dest='delta', action='store',
        help = 'Coverage convergence rate (default: 0.001)')
    opt_parser['CoreSet'].add_option('-o', '--output', default = 'test', type = 'str', dest='output_name', action='store',
        help = 'Output name prefix (default: test)')
    opt_parser['CoreSet'].add_option('-m', '--maf', default = 0, type = 'float', dest='maf', action='store',
        help = 'Minor allele frequency cut-off (default: 0.0)')

    # SelectVCF
    opt_parser['SelectVCF'].usage = "python run_genocore.py SelectVCF -i [VCF file] -g [Y or N (gziped)] -s [Sample list] -o [Output name] \n    Help: python run_genocore.py VCFtoCSV -h"
    opt_parser['SelectVCF'].add_option('-i', '--input', default = None, type = 'str', dest='input', action='store',
        help = 'Input vcf file')
    opt_parser['SelectVCF'].add_option('-g', '--gziped', default = 'N', type = 'str', dest='gziped', action='store',
        help = 'Wheter the VCf is gziped. Select "Y" or "N" (default:"N")')
    opt_parser['SelectVCF'].add_option('-s', '--sample', default = None, type = 'str', dest='sample', action='store',
        help = 'Sample text file (one sample per line)')
    opt_parser['SelectVCF'].add_option('-o', '--output', default = 'Selected.vcf', type = 'str', dest='output_name', action='store',help = 'Output selected vcf file name')



    # Get the command from sys.argv
    try:
        command = sys.argv[1]
    except IndexError:
        command = None

    # Get the appropriate option parser
    try:
        parser = opt_parser[command]
        # Done. Parse arguments and return.
        opts, args = parser.parse_args()
        return parser.parse_args()
    except KeyError:
        # Invalid command. Create a parser to show default usage
        parser       = optparse.OptionParser()
        parser.usage  = '\n\n%prog [Methods (VCFtoCSV or CoreSet or SelectVCF) ] [options]\n\n'
        parser.usage += 'Description:\n'
        parser.usage += '  This prgram works Python version 3 and requires Numpy library.\n'
        parser.usage += '  To work this program, select Methods, VCFtoCSV, CoreSet, or SelectVCF.\n\n'
        parser.usage += 'Commands for each methods:\n'
        for cmd in ['VCFtoCSV', 'CoreSet', 'SelectVCF']:
            parser.usage += '  %s\n' % cmd
            parser.usage += '    %s\n\n' % opt_parser[cmd].usage
        parser.usage = parser.usage.strip()
        if command is None:
            parser.error('command cannot be empty')
            sys.exit()
        else:
            parser.error('invalid command')
            sys.exit()

def main():
    options, args = parse_my_command_line()
    if len(args) != 1:
        print(os.system('python run_genocore.py -h'))
        sys.exit()
    return options, args

if __name__ == '__main__':
    opt, args = main()
    if args[0] == 'VCFtoCSV':
        if opt.input == None:
            print(os.system('python run_genocore.py VCFtoCSV -h'))
            sys.exit()
        infile = opt.input
        output = opt.output
        phased = opt.phased
        gziped = opt.gziped
        result = VCF_to_CSV(infile, output, phased, gziped)
        if result == "Done": 
            print("Coverting complete!")
        else:
            print("Coverting Error")
            sys.exit()

    if args[0] == "CoreSet":
        if opt.input == None:
            print(os.system('python run_genocore.py CoreSet -h'))
            sys.exit()
        infile = opt.input
        preset = opt.preset
        coverage = opt.coverage
        delta = opt.delta
        outname = opt.output_name
        maf = opt.maf 
        result = core_set(infile, preset, coverage, delta, outname, maf)
        if result == "Done":
            print("Core selection completed!")
        else:
            print("Core selection incompleted!")
            sys.exit()
  
    if args[0] == 'SelectVCF':
        if opt.input == None or opt.sample == None:
            print(os.system('python run_genocore.py SelectVCF -h'))
            sys.exit()
        infile = opt.input
        gziped = opt.gziped
        sample = opt.sample
        outname = opt.output_name
        result = VCF_select(infile, sample, outname, gziped)
        if result == "Done":
            print("VCF selection completed!")
        else:
            print("VCF selection incompleted!")
            sys.exit()
