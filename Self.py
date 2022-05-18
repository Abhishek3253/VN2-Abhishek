#self is not a key word we can use anything instead of self but not recomded
#self is reference variable always pointing to current object
#the first arguement to constructer and intsance always self 
# At the time of calling constructer or instance methode we are not required to pass any value 
#self variable internal PVM (python vertual Mechine ) provides values to self 
# The main purpose of self within a class to declare instance variable and access instance variable
#we cant use self out side the Class
class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks 
    
    def __str__(self):
        return f"{self.name} with the roll number {self.rollno} got {self.marks} marks"
    
  #  def talk(self):
     #   print("hello i am :",self.name)
     #   print("my roll no :",self.rollno)
     #   print("finally my Marks:",self.marks)
s1=Student('Abhi',401,95)
s2=Student('Anju',402,95)
print(s1)  
print(s2)  
