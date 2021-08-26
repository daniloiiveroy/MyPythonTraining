print("Hello Python's World")  # string with single quote\
print("Hello Python's World")  # string with double quote

# using variable in string
output = "Hello World"
print(output)

output = """Hello 
Python
World"""
print(output)  # multiline string

output = "Hello Python World"
print(len(output))  # get lenght funcntion

print(output[6])  # get specific char via index no

# word slicing
print(output[:5])
print(output[6:12])

# upper/lower case function
print(output.upper())
print(output.lower())

print(output.count("l"))  # count function

print(output.find("World"))  # find function

print(output.replace("World", "Universe"))  # replace function

# concatinates function
greeting = "Hello"
name = "Python"
print(greeting + ", " + name)

new_output = "{}, {}. Welcome!".format(greeting, name)
print(new_output)

new_output = f"{greeting}, {name.upper()}. Welcome!"
print(new_output)

print(dir(name))  # all functions for string

print(help(str.lower))  # help functions for string

person = {"Name": "Dan", "Age": 27}

### advance formatting ###
sentence = "My name is {0[Name]} and i am {0[Age]} years old.".format(person)
print(sentence)

sentence = "My name is {name} and i am {age} years old.".format(name="Dan", age="26")
print(sentence)

sentence = "My name is {Name} and i am {Age} years old.".format(**person)
print(sentence)

for i in range(1, 11):
    sentence = "The value is {:02}".format(i)
    print(sentence)

pi = 3.14159265
sentence = "Pi is equal to {:.4f}".format(pi)
print(sentence)

sentence = "1 MB is equal to {:,.2f} bytes".format(1000 ** 2)
print(sentence)

import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(my_date)

sentence = "{:%B %d, %Y}".format(my_date)
print(sentence)

sentence = "{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year".format(
    my_date
)
print(sentence)
"""
clear
& "D:/Program Files/Python39/python.exe" d:/Solutions/PythonTraining/00-string/app.py
& "C:/Python39/python.exe" E:/Solutions/PythonTraining/00-string/app.py
"""
