"""Create a function to calculate the compound interest for a given
principal amount, interest rate, and time."""
def ci(p,n,r):
    c =p*n*r/100
    return c
p=int(input('enter ->'))
r=int(input('enter->'))
n=int(input('enter->'))
print(ci(p,n,r))