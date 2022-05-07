a = str(input("enter the value of string :"))
c = {}
for i in a:
    if i in c.keys():
        c[i]+=1
    else:
     c[i]=1
print(c)
