student = {
    "Name" : "Dan",
    "Age" : 25,
    "Course" : ["Math" , "CompSci"]
}

print(student) #sample model
print(student["Course"]) #get specific key
print(student.get("Name")) #get method
print(student.get("Address")) #get method with error
print(student.get("Address","404 Not Found")) #get method with error and return message

#insert value with key
student["Address"] = "Bulacan"
print(student)

#update value
update_student = {
    "Name" : "Dan",
    "Age" : 27,
    "Course" : ["Math" , "CompSci"]
}

student.update(update_student)
print(student)

#delete key
del student["Address"]
print(student)

#pop function
age = student.pop("Age")
print(student)
print(age)

#lenght function
print(len(student))

#keys, values and items
print(student.keys())
print(student.values())
print(student.items())

#for loop
for key, value in student.items():
    print(key, value)

'''
clear
& "D:/Program Files/Python39/python.exe" d:/Solutions/PythonTraining/03-key-value/app.py
'''