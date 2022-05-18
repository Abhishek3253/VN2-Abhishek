str1 = str(input("enter the string  to reverse:"))
str2 = " " #empty string
for i in str1:
    str2=i+str2
print (str2)

#using user defined function
str1 = str(input("enter the string  to reverse:"))
def reverse(str1):
    str2=" "
    for i in str1:
        str2=i+str2
    return str2
    


print(reverse(str1))
