"""Create a function to find the smallest element in a list."""
def fact(n): 
   min=n[0] 
   for i in range(len(n)):
       if min>n[i]:
           min =n[i]
   return min
a=[3,4,8,3,2]
print(fact(a))