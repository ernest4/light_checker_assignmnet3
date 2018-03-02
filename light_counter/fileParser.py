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
                    #turn negative values to zero
                    instructions.append(pattern.match(line))
        
        #for debugging
        print(instructions)
        print(len(instructions))
        print(instructions[0].groups()[0])
        print(instructions[0].groups()[1])
        print(instructions[0].groups()[2])
        print(instructions[0].groups()[3])
        print(instructions[0].groups()[4])
        print(instructions[0].group())
        print(instructions[1].group())
        print(instructions[2].group())
                
        return size, instructions
        
        