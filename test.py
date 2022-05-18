row=int(input("Enter the values of Rows :"))
col=int(input("Enter the number of columns :"))
for i in range(row):
    for j in range(i,col):
       print(" " ,end =' ')
    for j in range(i+1):
        print("*",end =" ")
    print()