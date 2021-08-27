'''
phone = input("Phone: ")
output = ""
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

for ch in phone:
    output += digits_mapping.get(ch,"!") + " "
print(output)
'''
'''
def greet_user(name):
    print(f"Hi {name}!")
    print("Welcome aboard")

print("Start")
greet_user(input("Your name: "))
print("Finish")
'''
'''

def square(number):
    return number * number

output = square(int(input("Square of:")))
print("The value is",output)
'''
'''
import utils

numbers = [10,3,6,2]
maximum = utils.find_max(numbers)

print(maximum)
'''

'''
import random

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second

dice = Dice()
print(dice.roll())
'''

from pathlib import Path

path = Path()
for file in path.glob("*.py"):
    print(file)

'''
clear
& python d:/Solutions/PythonTraining/99-PythonExercises/app.py
'''