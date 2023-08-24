def fib(n):
    a=0;b=1
    for i in range(n):
        print(a)
        a=a+b
        a,b=b,a
n=int(input('enter the number->'))
fib(n)