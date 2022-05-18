#vendor shop code to check and excute the control statement 
av=10
x=int(input("enter the value x:"))
i=1
while i<=x:
    if av<x:
        print("out of stock ")
        break
    print (" candy ")
    i+=1
else:
    print("thank and visit again")


#continue
#print not  divisable by 3
for i in range (1,101): 
    if i%3==0:
        continue
    else:
        print(i ,end =" ")



#pass
for i in range (10):
    if i%2!=0:
        pass
    else:
        print(i)
