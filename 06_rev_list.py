def fact(a,n): 
    for i in range(5,-1,-1):
        n.append(a[i])
    return n      
a=[3,5,6,5,3,7]
n=[]
print(fact(a,n))