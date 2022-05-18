#Pattern Programs 

####print Square ####
row=int(input("Enter the values of Rows :"))
col=int(input("Enter the number of columns :"))
for i in range(row): #print Rows - here i incates Rows position 
    for j in range(col): #print column - here j incates Rows position column 
       print("*" ,end =' ')
    print()            #helps jumps to next row 


#to print raising traingle 
row=int(input("Enter the values of Rows :"))
col=int(input("Enter the number of columns :"))
for i in range(row):
    for j in range(i+1):
       print("*" ,end =' ')
    print()


#Decreasing Traingle 

row=int(input("Enter the values of Rows :"))
col=int(input("Enter the number of columns :"))
for i in range(row):
    for j in range(i,col):
       print("*" ,end =' ')
    print()