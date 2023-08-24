# Write a function that finds the maximum value in a list of numbers.
      

def fact(n): 
   max=n[0] 
   for i in range(len(n)):
       if max>n[i]:
           max =n[i]
           return max
a=[3,4,8,3,2]
print(fact(a))