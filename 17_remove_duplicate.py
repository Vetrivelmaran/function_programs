def duplicat(n):
    new=[]
    for i in n:
        if i not in new:
            new.append(i)
    return new
a=[2,5,6,8,4,2,1]
print(duplicat(a))