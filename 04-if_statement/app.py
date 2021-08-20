#if condition
if True:
    print("Condition is true")

if False:
    print("Condition is false")

#Comparisons
#Equals
language = "Python"
if language == "Python":
    print("Condition is true")

#Not Equal
if language != "Python":
    print("Condition is true")
else:
    print("Condition is false")

#Else if
if language == "Java":
    print("The programming language is Java")
elif language == "C#":
    print("The programming language is C#")
else:
    print("The programming language is Python")

#and
#or
#not
user = "Admin"
logged_in = False

if user == "Admin" and logged_in:
    print("You are admin")
else:
    print("Not Admin")

if user == "Admin" or logged_in:
    print("You are admin")
else:
    print("Not Admin")

if not logged_in:
    print("Not Admin")
else:
    print("You are admin")

#List comparisons
a = [1,2,3,4]
b = [1,2,3,4]

print(a == b)
print(a is b)
print(id(a))
print(id(b))

num1 = 1
num2 = 1
print(num1 is num2)

#False values

#False
condition = False
if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

#None
condition = None
if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

#Zero of any numeric type
condition = 0
if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

#any empty sequence. for example "" ,(), []
condition = ()
if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

#any empty mapping. for example {}
condition = {}
if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

'''
clear
& "D:/Program Files/Python39/python.exe" d:/Solutions/PythonTraining/04-if_statement/app.py
'''