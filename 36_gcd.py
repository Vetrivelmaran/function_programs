def gcd(a,b):
    for i in range(a,b+1):
        if a%i==0 and b%i==0:
            gcd=i
            break
    return gcd            
print(gcd(4,8))