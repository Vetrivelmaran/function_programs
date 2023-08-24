"""Write a function that calculates the power of a number raised to
an exponent."""
def pow(base,e):
    sum=1
    for i in range(e):
        sum=sum*base
    return sum
print(pow(2,3))
        