import datetime

d = datetime.date(2016, 7 , 24)

print(d) #normal date

today = datetime.date.today()

print(today) #date today
print(today.year) #date year
print(today.day) #date day
print(today.weekday()) #date weekday
print(today.isoweekday()) #date weekday

deltatime = datetime.timedelta(days=7)
print(today + deltatime)

bday = datetime.date(2022, 1, 4)
til_bday = bday - today
print(til_bday.days) #days
print(til_bday.total_seconds()) #days

time = datetime.time



'''
clear
& "D:/Program Files/Python39/python.exe" d:/Solutions/PythonTraining/09-datetime/app.py
'''