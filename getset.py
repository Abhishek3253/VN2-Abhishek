class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks

n = int (input("Enter the no of students : "))
students =[]
for i  in range(n):
    s=Student()
    name=input("enter the student name :")
    marks=int(input("enter the Marks :"))
    s.setName(name)
    s.setMarks(marks)
    students.append(s)
for s in students:
    print("hello",s.getName())
    print("yours Marks is ",s.getMarks())
    print()
