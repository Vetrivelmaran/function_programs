def check(str):
    count=0
    for i in range(len(str)):
        if int(i)>=0 and int(i)<=9:
            count+=1
    if count==len(str):
        return 'yes'
    else:
        return 'not'
str ='123'
result =check(str)
print(result)