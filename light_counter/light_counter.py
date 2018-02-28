# -*- coding: utf-8 -*-

import sys, getopt

"""
Main module.

Inspired by the lecture notes.
"""
class LightTester:
    lights = None
    
    def __init__(self, size):
        self.lights = [[False]*size for _ in range(size)]
        
    def apply(self, command):
        pass
    
    def count(self):
        pass

def main(argv):
    pass

if __name__ == "__main__":
    main(sys.argv[1:])