"""Write a function that calculates the sum of digits in a given
integer."""
def sum(n):
    som=0
    for i in str(n):
        som+=int(i)
    return som

n=int(input(('enter the num->')))
result =sum(n)
print(result)
