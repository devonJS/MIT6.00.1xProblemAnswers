"""
Finds the 'polysum' of a polygon, area plus perimeter squared
n is the number of sides a polygon has, integer
s is the length of each side of the polygon, float or integer 
"""

import math

def polysum(n, s):
    area = (0.25 * n * s ** 2) / math.tan(math.pi / n)
    perimeter_squared = (n * s) ** 2
    return round(area + perimeter_squared, 4)