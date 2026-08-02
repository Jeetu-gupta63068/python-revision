class student:
    college_name="abc college"
    name="anonymous"
    def __init__(self,name,marks):
        self.name= name
        self.marks= marks
        print("adding new sudnet in database:")
        
s1= student("jitu",98)
print(s1.name)

s2=student("jitu",98)
print(s1.marks)