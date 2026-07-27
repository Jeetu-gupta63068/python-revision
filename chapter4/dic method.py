student={
    "name":"Jitu Gupta",
    "subject":{
        "phy":98,
        "chem":98.0,
        "math":94
    }
} 

print(list(student.values()))
print(student.items())
print(student.get("name"))
new_dict={"city": "delhi", "age":16}
student.update(new_dict)
print(student)