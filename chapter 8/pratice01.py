class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        return sum(self.marks) / len(self.marks)

s1 = Student("Jitu Gupta", [98, 97, 96])

print("Name:", s1.name)
print("Marks:", s1.marks)
print("Average:", s1.get_average())