n=int(input(" enter the value of N :"))
for i in range(2,n):
    if n%i==0:\
        print("Not a prime number :")
    break
else:
    print(" Given number is a Prime : ")
