# -*- coding: utf-8 -*-

import sys
import optparse
from ast import parse

"""
Main module.

Inspired by the lecture notes.
"""
def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
        
    if len(argv) < 1:
        print("Usage: --input <input file or link>")
        sys.exit(2)
        
    parser = optparse.OptionParser()
    parser.add_option('--input', dest="inputFileName", help="input file to be processed")
    
    opts, args = parser.parse_args(argv)
    
    print(opts.inputFileName)

if __name__ == "__main__":
    main()