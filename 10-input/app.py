#### input function
"""
name = input("What is your name?")
print(name)

birth_year = input("Birth year: ")
age = 2021 - int(birth_year)
print(age)

w_lbs = input("What is your weight(in lbs)?")
w_kg = int(w_lbs) * 0.45359237
print(w_kg)
"""

#### input chars validation
"""
name = input("What is your name?")
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Awesome name", name)
"""

#### input convertion
"""
weight = int(input("Weight: "))
metric = input("(L)bs or (K)g: ")
output = 0

if metric.upper() == "K":
    output = weight / 0.45359237
    print(f"You are {output} kilogram.")
elif metric.upper() == "L":
    output = weight * 0.45359237
    print(f"You are {output} pounds.")
else:
    print("Please choose proper weight/metric.")
"""

#### input while loop break
"""
secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("You loser!")
"""
#### input game excercise
print("start - to start car")
print("stop - to stop car")
print("quit - to exit")

car_status = ""
memory_status = ""
while True:
    car_status = input(">").lower()
    if car_status == "start":
        print("Car started....Ready to go!")
    elif car_status == "stop":
        print("Car stopped.")
    elif car_status == "help":
        print(
            """
start - to start car
stop - to stop car")
quit - to exit"""
        )
    elif car_status == "quit":
        break
    else:
        print("I don't understand that...")

    memory_status = car_status
"""
clear
& "D:/Program Files/Python39/python.exe" d:/Solutions/PythonTraining/09-input/app.py
& "C:/Python39/python.exe" E:/Solutions/PythonTraining/09-input/app.py
"""
