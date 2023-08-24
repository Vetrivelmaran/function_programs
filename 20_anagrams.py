def angrams(s1,s2):
    o=sorted(s1)
    p=sorted(s2)
    if o==p:
        return 'yes angram'
    else:
        return 'not'
    
n=angrams('mama','amma')
print(n)