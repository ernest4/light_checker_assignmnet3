# -*- coding: utf-8 -*-

import sys
import optparse
from ast import parse
from light_counter.lightTester import LightTester
from light_counter.fileParser import fileParser

"""
Main module.

Inspired by the lecture notes.
"""
def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
        
    #argument error handling
    if len(argv) < 1 or argv[0] != '--input':
        print("Usage: --input <input file or link>")
        sys.exit(2)
        
    #parsing command line arguments
    parser = optparse.OptionParser()
    parser.add_option('--input', dest="inputFileName", help="input file to be processed")
    
    opts, args = parser.parse_args(argv)
    
    #parsing the input file
    size, instructions = fileParser(opts.inputFileName)
    
    if size is None or instructions is None: #Invalid size or no valid instructions available
        sys.exit(2)
    
    #creating a light tester class, applying the instructions and printing the result
    print("Processing: ", opts.inputFileName)
    lightTester = LightTester(size)
    
    for instruction in instructions:
        lightTester.apply(instruction)
        
    
    print("Results for: ", opts.inputFileName, "\n#occupied: ", lightTester.count())
    return 0

if __name__ == "__main__":
    main()