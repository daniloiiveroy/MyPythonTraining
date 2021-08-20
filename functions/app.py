#function
def hello_func():
    print("Hello Function!")

hello_func()

#function with return
def return_func():
    return "Return Function"

print(return_func())
print(len(return_func()))
print(return_func().upper())

#function with arguments
def return_func(greeting):
    return f"{greeting} Function"

print(return_func("Hi"))

#function with default value
def default_func(greeting, name = "You"):
    return f"{greeting}, {name}"

print(default_func("Hi"))
print(default_func("Hi", name="DAN"))

#tuple and dictionary
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info("Math","Art", Name="Dan",Age = 27)

#passing tuple and dictionary
courses = ["Science","History"]
info = { "Name": "Alou","Age": 25 }

student_info(*courses,**info)

#functions training
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_leap(year):
    '''return True for leap year, false for non-leap year'''

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    '''return number of days in that month in that year'''

    if not 1 <= month <= 12:
        return "Invalid Month"
    
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]

print(days_in_month(2016,2))
'''
clear
& "D:/Program Files/Python39/python.exe" d:/Solutions/PythonTraining/functions/app.py
'''