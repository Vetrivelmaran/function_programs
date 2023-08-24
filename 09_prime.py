def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False
n=int(input('entr'))
if prime(n):
    print('prime')
else:
    print('not ')