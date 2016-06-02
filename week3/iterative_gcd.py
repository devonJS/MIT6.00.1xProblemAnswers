def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    gcd = 0
    value = 0
    if(a < b):
        value = a
    elif(a > b):
        value = b
    
    while gcd == 0:
        if(a % value == 0 and b % value == 0):
            gcd = value
        else:
            value -= 1
            
    return gcd

print(gcdIter(18, 84)) # Expects 6
print(gcdIter(132, 275)) # Expects 11
print(gcdIter(198, 108)) # Expects 18
print(gcdIter(408, 374)) # Expects 34
print(gcdIter(360, 270)) # Expects 90