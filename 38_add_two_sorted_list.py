def merg(l1,l2):
    new=l1+l2
    for i in range(len(new)):
        for j in range(i+1,len(new)):
            if new[i]>new[j]:
                new[i],new[j]=new[j],new[i]
    return new
l1=[3,4,7]
l2=[5,1,8]
print(merg(l1,l2))