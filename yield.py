#Yield function is generater function used in advanced python to resume or hold the 
#values to in program and we can access result when we want generator 

lst1 =[2,3,4,5]
def sqrt(lst1):
    for each in lst1:
        yield(each**2) #yield fuction  to hold or resume the result 

result = list(sqrt(lst1))
print(result)

#without using yield 
lst1 =[2,3,4,5]
def sqrt(lst1):
    lst2=[] #temp lis yto store the result
    for each in lst1: # for loop used To iterate elements in List 
        lst2.append(each**2) # logic to find sqare of each elements in list1 and store result in list 2
    return lst2

result = sqrt(lst1)
print (result)
