"""Implement a function that checks if a list is sorted in ascending
order."""
def check(a):
    count=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]<a[j]:
                count+=1
                break
    if count==len(a)-1:
        return 'assendin'
    else:
        return 'desending'
n=[2,4,6,32,3]
print(check(n))