"""Implement a function that checks if a given string is a valid email
address"""
def check(a):
    for i in a[0:2:1]:
        if i==i.lower():
            return 'valide'
        else:
            return 'not valid'
        
    
a=input('->')
print(check(a))



