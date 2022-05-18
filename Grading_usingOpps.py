class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks 
    def display(self):
        return f"{self.name}  got {self.marks} marks"
    def Grade(self):
        if self.marks >= 60 :
            print ("First Class")
        elif self.marks >=50 :
            print("Second class")
        elif self.marks>=35 :
            print("Pass")
        else:
            print("Fail")

n=int(input("Enter the number of students: "))
for i in range(n):
    name=input("Enter the name :")
    marks = int(input("enter the Marks "))
    s=Student(name,marks)
    s.display()
    s.Grade()
    print()