'''
Created on 28 Feb 2018

@author: ernest
'''

import numpy as np

class LightTester:
    """
    This class is a container for two dimensional light grid with methods to modify the grid and return the element count.
    """
    lights = None #!!! PUBLIC for testing purposes, make PRIVATE once tests are done !!!
    
    def __init__(self, size):
        #self.lights = [[False]*size for _ in range(size)]
        self.lights = np.array([[False]*size for _ in range(size)])
        
    def apply(self, command):
        action, x1, y1, x2, y2 = command[0], command[1], command[2], command[3], command[4]
        #print(action,',',x1,',',y1,',',x2,',',y2) #Testing information, printing commands
        if command[0] == "turn on":
            for row in range(len(self.lights)):
                for col in range(len(self.lights[row])):
                    if y2 >= row >= y1 and x2 >= col >= x1:
                        self.lights[row,col] = True
        elif command[0] == "turn off":
            for row in range(len(self.lights)):
                for col in range(len(self.lights[row])):
                    if y2 >= row >= y1 and x2 >= col >= x1:
                        self.lights[row,col] = False
        else: #switch
            for row in range(len(self.lights)):
                for col in range(len(self.lights[row])):
                    if y2 >= row >= y1 and x2 >= col >= x1:
                        if self.lights[row,col] == True:
                            self.lights[row,col] = False
                        else:
                            self.lights[row,col] = True
    
    def count(self): #count the number of lights which are on
        count = 0
        for row in range(len(self.lights)):
            for col in range(len(self.lights[row])):
                if self.lights[row,col] == True:
                    count += 1
        return count