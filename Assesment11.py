#Traversing the elements of List:
#using for loop
lst1=[1,2,3,4,5]
for each in lst1:
    print(each)
#using while loop
lst1=[1,2,3,4,5]
l=len(lst1)
i=0
while i<l :
    print(lst1[i])
    i+=1

#3. To display only even numbers:
lst1=[1,2,3,4,5]
for each in lst1:
    if each%2==0:
        print(each)
    else:
        pass
#To display elements by index wise(-Ve, +ve):
 
lst1 =[1 ,2 ,3 ,-4 ,-6]
print("original list " , lst1)
l=len(lst1)
print ("indexed list :" )
for i in range(l):
    print (i,end =" ")
    print (str(lst1[i]))
#I. To get information about list: Len(),count(),index()
lst1 =[1 ,2 ,3 ,-4 ,-6 ,3 , 4]
l=len(lst1)
c=lst1.count(3)
print(" Example len() :" ,l)
print(" Example count() :" ,c)
print(" Example Index() :" ,lst1.index(4))

# Manipulating elements of List:insert() ,apppend(),extend()
lst1 =[1 ,2 ,3 ,4 ,5]
lst2=["hi" , "learn" ,"python"]
lst1.append(lst2)
lst2.insert(1,"Abhishek")
lst2.extend(lst1)

# List -Ordering elements of List:
lst1 =[4,3,6,8,1,5,7,2]
lst1.sort()
print(lst1)
lst1.reverse()
print(lst1)

# Aliasing and Cloning of List objects:
a = [81, 82, 83]
b = [81, 82, 83]
print(a == b)
print(a is b)
b = a
print(a == b)
print(a is b)
b[0] = 5
print(a)



