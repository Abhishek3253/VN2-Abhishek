#without using in bulitfunction 
x= str(input("Enter the string : "))
y=""
for i in x:
    y=i+y
if y==x:
    print("yes",y,"is palindrome")
else:
    print("not",y,"is not a palindrome")

#using bulit in Function 
x= str(input("Enter the string : "))

def pali():
    if x==x[::-1]:
        print("Palindrom")
    else:
        print("not palindrom")

pali()