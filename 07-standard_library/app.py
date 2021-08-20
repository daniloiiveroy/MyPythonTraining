import module as mod
from module import find_index
import sys
import random
import math
import datetime
import calendar
import os
import antigravity

sys.path.append("d:\Solutions\PythonTraining\modules") #importing outside dir

courses = ["History", "Math", "Physics", "CompSci"]

#import module
index = mod.find_index(courses,"Physics")
print(index)

#from module import
print(find_index(courses,"CompSci"))

#sys library
print(sys.path)

#random library
print(random.choice(courses))

#math library
rads = math.radians(90)
print(rads)
print(math.sin(rads))

#datetime library
today = datetime.date.today()
print(today)

#calendar library
print(calendar.isleap(2020))

#os library
print(os.getcwd())

#locate files
print(os.__file__)

#antigravity
antigravity
'''
clear
& "D:/Program Files/Python39/python.exe" d:/Solutions/PythonTraining/07-standard_library/app.py
'''