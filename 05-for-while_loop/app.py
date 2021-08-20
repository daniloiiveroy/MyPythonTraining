nums = [1, 2, 3, 4, 5]

#for loop
print("### Start ###")
for num in nums:
    print(num)
print("### End ###")

#for loop break
print("### Start ###")
for num in nums:
    if num == 4:
        break
    print(num)
print("### End ###")

#for loop continue
print("### Start ###")
for num in nums:
    if num == 4:
        print("Skipped")
        continue
    print(num)
print("### End ###")

#nested for loop
print("### Start ###")
for num in nums:
    for letter in "ABC":
        print(num, letter)
print("### End ###")

#range function
print("### Start ###")
for i in range(10):
    print(i)
print("### End ###")

#range start at index function
print("### Start ###")
for i in range(1, 10):
    print(i)
print("### End ###")

#while loop
x = 1
print("### Start ###")
while x <= 10:
    print(x)
    x += 1
print("### End ###")

#while loop with break
x = 1
print("### Start ###")
while x <= 10:
    if x == 6:
        break
    print(x)
    x += 1
print("### End ###")

#while loop with infinite loop with CTRL C
x = 1
print("### Start ###")
while True:
    print(x)
    x += 1


'''
clear
& "D:/Program Files/Python39/python.exe" d:/Solutions/PythonTraining/05-for-while_loop/app.py
'''