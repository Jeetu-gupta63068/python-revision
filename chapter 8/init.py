class Student:
    def __init__(self, fullname):
        self.name = fullname
        print("Adding new student in database")

s1 = Student("Karan")
print(s1.name)

s2= Student("jitu")
print(s2.name)