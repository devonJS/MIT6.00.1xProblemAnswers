def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''

    if b == 0:
        return a
    else:
        i = 1
        high = 0
        low = 0
        if(a > b):
            high = a 
            low = b
        else:
            high = b
            low = a

        # Euclidean algorithm, if the remainder of the high divided by low is greater than low,
        # increase the multiplier of the low by 1 until the remainder is less than the lower number
        # keep doing this until the remainder is 0, the low number is then the gcdIter
        
        remainder = high % (low * i)
        while remainder > low:
            remainder = high % (low * i)
            i += 1
            
        if remainder == 0:
             return low
        else: 
             return gcdRecur(low, remainder)
 
print(gcdIter(18, 84)) # Expects 6
print(gcdIter(132, 275)) # Expects 11
print(gcdIter(198, 108)) # Expects 18
print(gcdIter(408, 374)) # Expects 34
print(gcdIter(360, 270)) # Expects 90