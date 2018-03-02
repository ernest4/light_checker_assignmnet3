import re
import sys
from unittest import result
import requests

def fileParser(inputURI):
    '''
    Parses an input file URI to find and extract valid commands.
    '''
    pattern = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
    
    size, instructions = None, []
    
    if inputURI.startswith("http"):
        #process URL
        req = requests.get(inputURI).text
        
        returnedStringList = '\n'.join(req.split('\n')).splitlines()
        
        #print(returnedStringList[1:3])
        
        try:
            size = int(returnedStringList[0])
        except ValueError:
            print("Input file "+inputURI+" has non integer size for the lights matrix.")
            return None, None
        
        for line in returnedStringList[1:]:
            result = pattern.match(line)
            if result is not None:
                result = list(result.groups())
                #convert numbers to ints
                for i in [1,2,3,4]:
                    result[i] = int(result[i])
                #turn negative values to zero
                for i in [1,2,3,4]:
                    if result[i] < 0:
                        result[i] = 0
                instructions.append(result)
    else:
        #process local file
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
                        result[i] = int(result[i])
                    #turn negative values to zero
                    for i in [1,2,3,4]:
                        if result[i] < 0:
                            result[i] = 0
                    instructions.append(result)
                
    return size, instructions
        
        