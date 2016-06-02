'''
The isIn method uses recursion and bisection search to find if a character
is in an alphabetized string (aStr)
'''

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False
    
    if len(aStr) == 0:
        return False
        
    halfIndex = int(len(aStr) / 2)
    
    if char == aStr[halfIndex]:
        return True
    elif char < aStr[halfIndex]:
        return isIn(char, aStr[0:halfIndex])
    elif char > aStr[halfIndex]:
        return isIn(char, aStr[halfIndex:])
        
print(isIn('m', 'dgjlmoptuvvwz')) # Expects True
print(isIn('c', 'hijmstuyz')) # Expects False
print(isIn('g', 'acdeeffghinnnqqrtvyz')) # Expects True