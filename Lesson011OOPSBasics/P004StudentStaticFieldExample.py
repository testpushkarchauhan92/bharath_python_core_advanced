class Student:
    # static field which is common for all objects
    major = "CSE"

    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name

s1=Student(1,"Pushkar")
s2=Student(2,"Adam")
print(s1.major)
print(s2.major)
print(s1.name)
print(s2.name)
print(Student.major)
