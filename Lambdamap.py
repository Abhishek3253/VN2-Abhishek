#using map 
lst1 =[2 ,4 ,5]
def sqrt(x):
    return x*x
print(list(map(sqrt ,lst1)))

#using lambda 
lst1 = [2,3,6,5]
result =  list(map(lambda x:x*x ,lst1))
print (result)