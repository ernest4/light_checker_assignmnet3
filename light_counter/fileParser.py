
def fileParser(inputURI):
    '''
    Parses an input file URI to find and extract valid commands.
    '''
    
    if inputURI.startswith("http"):
        #process URL
        return None, None
    else:
        #process local file
        return None, None
        
        