"""Implement a function that converts a list of integers to a single
integer (e.g., [1, 2, 3] -> 123)."""
def str_to_int(l):
    sum=0
    for i in l:
        sum=sum*10+i
    return sum
l=[1,2,3]
print(str_to_int(l))