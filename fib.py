def fib(n):
    a , b = 0 , 1
    sum = 0
    if n <= 0:
        print(" enter the valid number :")
    else:
        for i in range(2 ,n):
            sum=a+b
            print(sum , end=" ")
            a=b
            b=sum

        
fib(9)