"""Implement a function to find the area of a triangle given its base
and height."""
def triangle(b,h):
    return int(1/2*b*h)

b=int(input('enter ->'))
h=int(input('enter ->'))
print(triangle(b,h))

