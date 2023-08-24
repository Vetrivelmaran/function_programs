def sec(a):
    for i in range(len(n)):
        for j in range(i+1,len(a)):
            if n[i]>n[j]:
                n[i],n[j]=n[j],n[i]
    return n[-2]  
    
    
n=[2,4,6,32,3]
print(sec(n))