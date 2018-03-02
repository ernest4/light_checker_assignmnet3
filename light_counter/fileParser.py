import re
import sys
from unittest import result

def fileParser(inputURI):
    '''
    Parses an input file URI to find and extract valid commands.
    '''
    pattern = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
    
    if inputURI.startswith("http"):
        #process URL
        return None, None
    else:
        #process local file
        size, instructions = None, []
        with open(inputURI, 'r') as inputFile:
            try:
                size = int(inputFile.readline())
            except ValueError:
                print("Input file "+inputURI+" has non integer size for the lights matrix.")
                return None, None
            for line in inputFile.readlines():
                result = pattern.match(line)
                if result is not None:
                    result = list(result.groups())
                    #convert numbers to ints
                    for i in [1,2,3,4]:
                        print("iterator",i)
                        result[i] = int(result[i])
                    #turn negative values to zero
                    for i in [1,2,3,4]:
                        if result[i] < 0:
                            result[i] = 0
                    instructions.append(result)
        
        #for debugging
        print(instructions)
        print(len(instructions))
        print(instructions[0][0])
        print(instructions[0][1])
        print(instructions[0][2])
        print(instructions[0][3])
        print(instructions[0][4])
        print(instructions[0])
        print(instructions[1])
        print(instructions[2])
                
        return size, instructions
        
        