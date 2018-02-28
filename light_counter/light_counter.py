# -*- coding: utf-8 -*-

import sys, getopt

"""
Main module.

Inspired by the lecture notes.
"""
class LightTester:
    lights = None #!!! PUBLIC for testing purposes, make PRIVATE once tests are done !!!
    
    def __init__(self, size):
        self.lights = [[False]*size for _ in range(size)]
        
    def apply(self, command):
        action, x1, y1, x2, y2 = command[0], int(command[1]), int(command[2]), int(command[3]), int(command[4])
        print(action,',',x1,',',y1,',',x2,',',y2) #Testing information
        if command[0] == "turn on":
            for row in range(len(self.lights)):
                for col in range(len(self.lights[row])):
                    if y2 >= row >= y1 and x2 >= col >= x1:
                        self.lights[row][col] = True
        elif command[0] == "turn off":
            for row in range(len(self.lights)):
                for col in range(len(self.lights[row])):
                    if y2 >= row >= y1 and x2 >= col >= x1:
                        self.lights[row][col] = False
        else: #switch
            for row in range(len(self.lights)):
                for col in range(len(self.lights[row])):
                    if y2 >= row >= y1 and x2 >= col >= x1:
                        if self.lights[row][col] == True:
                            self.lights[row][col] = False
                        else:
                            self.lights[row][col] = True
    
    def count(self):
        count = 0
        rowLengthsList = [len(row) for row in self.lights]
        for length in rowLengthsList:
            count += length
        return count

def main(argv):
    pass

if __name__ == "__main__":
    main(sys.argv[1:])