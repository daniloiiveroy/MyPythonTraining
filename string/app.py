print('Hello Python\'s World') #string with single quote\
print("Hello Python's World") #string with double quote

#using variable in string
output = "Hello World"
print(output)

output = """Hello 
Python
World"""
print(output) #multiline string

output = "Hello Python World"
print(len(output)) #get lenght funcntion

print(output[6]) #get specific char via index no

#word slicing
print(output[:5])
print(output[6:12])

#upper/lower case function
print(output.upper())
print(output.lower())

print(output.count("l")) #count function

print(output.find("World")) #find function

print(output.replace("World","Universe")) #replace function

#concatinates function
greeting = "Hello"
name = "Python"
print(greeting + ", " + name)

new_output = "{}, {}. Welcome!".format(greeting,name)
print(new_output)

new_output = f"{greeting}, {name.upper()}. Welcome!"
print(new_output)

print(dir(name)) #all functions for string

print(help(str.lower)) #help functions for string


'''
clear
& "D:/Program Files/Python39/python.exe" d:/Solutions/PythonTraining/string/app.py
'''