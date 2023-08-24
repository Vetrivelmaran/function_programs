"""Implement a function to calculate the area of a triangle given its
three sides (Heron's formula)."""
import math
def area(a,b,c):
    s=a+b+c//2
    new=s*(s-a)*(s-b)*(s-c)
    are =math.sqrt(new)
    return are
print(area(7,6,5))