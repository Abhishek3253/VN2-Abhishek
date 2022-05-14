marks=int(input(" Enter the Marks of the candidate :"))
if marks>90 and marks<100 :
    print ("grade is -- A+")
elif marks>80 and marks<=90 :
    print (" Grade is -- A")
elif marks>60 and marks<=80 :
    print ('Grade is -- B+')
elif marks>45 and marks<=60 :
    print(" Grade is -- B")
else:
    print("Fail")

