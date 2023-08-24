"""def long(a):
    max=len(a[0])
    for i in a:
        if max<len(i):
            max=len(i)
            word=i
    return max,word
a=['vteri','hi','kamalsd']
print(long(a))    """

def check(a):
    count=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if len(a[i])<len(a[j]):
                count+=1
                break
    if count==len(a)-1:
        return 'assendin'
    else:
        return 'desending'
a=['vteri','hi','kamalsd']
print(check(a))