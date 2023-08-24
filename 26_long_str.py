def long(a):
    max=len(a[0])
    for i in a:
        if max<len(i):
            max=len(i)
            word=i
    return max,word
a=['vteri','hi','kamalsd']
print(long(a))    