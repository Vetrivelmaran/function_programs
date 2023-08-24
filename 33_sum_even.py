"""Write a function that calculates the average of all even numbers in
a list."""
def avg(a,som): 
    for i in a:
        if i%2==0:
          som=som+i
    return som/len(a)
a=[3,5,6,5,3,7]
print(avg(a,0))
