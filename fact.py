from re import I


n=int(input("enter the value of N : "))
def fact(n):
    if n<=0:
        return 1
    else:
        n=n*fact(n-1)
    return n 

factorial =fact(n)
print (factorial)

n=int(input("enter the value of N : "))
fact = 1
if n<=0:
    print(1)
else:
    for each in n:
        fact=fact*each

print(fact)


