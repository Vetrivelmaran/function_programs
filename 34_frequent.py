def fre(a):
    a=max(a,key=a.count)
    return a
a=[3,5,6,5,3,7]
print(fre(a))