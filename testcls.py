class Student:
    def __init__(self,name,age , marks):
        self.name=name
        self.age=age
        self.marks=marks

    def talk(self):
        print("hello My name is :", self.name)
        print("my age is :" ,self.age)
        print("My marks is " ,self.marks)

s1=Student('Abhishek' , 26 , 80  )
s2=Student("Anjali" , 26 ,90 )
s1.talk()
s2.talk()




