from typing_extensions import TypeVarTuple


courses = ["History", "Math", "Physics", "CompSci"]
print(courses) #List
print(courses[2]) #Specific course via index
print(courses[-1]) #Last item

print(courses[0:2]) #List of items
print(courses[2:]) #List of items

#Append function
courses.append("Art I")
print(courses)

#Insert function
courses.insert(1,"Art II")
print(courses)

#Insert List function Adding list
new_courses = ["Computer", "Science"]
courses.insert(-1,new_courses)
print(courses)

#Extend function Adding value at the end
new_courses = ["Filipino", "MAPEH"]
courses.extend(new_courses)
print(courses)

#Remove Function
courses.remove(("Filipino"))
courses.remove(("Art I"))
print(courses)

#Pop Function Removing last value in list
courses.pop()
print(courses.pop())
print(courses)

#Reverse Function
courses.reverse()
print(courses)

#Sort Function
sort_courses = courses
sort_courses.sort()
print(sort_courses)

nums = [3, 5, 4, 1, 2]
nums.sort()
print(nums)

#Sort Reverse Function
sort_courses.sort(reverse=True)
print(sort_courses)

#Sort without altering original list Function
print(sorted(courses))

#Min, Max and Sum Function
print(min(nums))
print(max(nums))
print(sum(nums))

#Search function
print(courses.index("CompSci"))

#Search if exist
print("Math" in courses)

#for loop function
for course in courses:
    print(course)

#for loop with enumerate function
for course in enumerate(courses):
    print(course)

for index, course in enumerate(courses):
    print(index, course)

#for loop with index start
for index, course in enumerate(courses,start=1):
    print(index, course)

#list to string
course_str = ", ".join(courses)
print(course_str)

#split string function
print(course_str.split(", "))


list_1 = ["History", "Math", "Physics", "CompSci"]
list_2 = list_1

print(list_1)
print(list_2)

#replacing list data via index
list_1[0] = "Art III"
print(list_1)
print(list_2)

#tuples
tuple_1 = ("History", "Math", "Physics", "CompSci")
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

#replacing list data via index
#tuple_1[0] = "Art III"
print(tuple_1)
print(tuple_2)

#Sets removes duplicate data
cs_courses = {"History", "Math", "Physics", "CompSci", "Math"}
print(cs_courses)

#set searching
print("Math" in cs_courses)

#intersection like inner join
it_courses = {"Boilogy", "Math", "Chemistry", "CompSci"}
print(cs_courses.intersection(it_courses))

#union function
print(cs_courses.union(it_courses))

#empty lists
empty_list = []
empty_list = list()

#empty tuples
empty_tuple = ()
empty_tuple = tuple()

#empty sets
empty_set = {} #this isn't right! It's a dict
empty_set = set()


'''
clear
& "D:/Program Files/Python39/python.exe" d:/Solutions/PythonTraining/02-lists_tuples_sets/app.py
'''