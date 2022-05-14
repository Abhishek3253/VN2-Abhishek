#user defined function
def Prime(n):
    if (n==1 and n==0):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

#driver fuction 
n=int(input("Enter the Range to print :"))
for i in  range(1 ,n+1):
    if(Prime(i)):
        print(i,end=" ")







