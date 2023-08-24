def fact(n):
    if n%2==0:
        return 'even'
    else:
        return 'odd'
a=int(input(('enter the num->')))
print(fact(a))