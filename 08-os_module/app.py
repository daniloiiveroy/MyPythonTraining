import os

#help check
#print(dir(os))

#get working dir
print(os.getcwd())

#changing dir
os.chdir("d:/Solutions/PythonTraining/")
print(os.getcwd())

#list of dir
print(os.listdir())

#create folder
#os.makedir("main_dir/sub_dir") #if main not exist dir cant create
#os.makedirs("main_dir/sub_dir/")

#remove folder
#os.rmdir("main_dir/sub_dir") #if main not exist dir cant delete
#os.removedirs("main_dir/sub_dir")

#rename files
os.chdir("d:/Solutions/PythonTraining/main_dir/sub_dir/")
#os.rename("test.txt","demo.txt")
#print(os.listdir())

#file info
print(os.stat("demo.txt").st_size)
print(os.stat("demo.txt").st_mtime)
from datetime import datetime
mod_time = os.stat("demo.txt").st_mtime
print(datetime.fromtimestamp(mod_time))

#walk dir
os.chdir("d:/Solutions/PythonTraining/")

for dirpath, dirnames, fileames in os.walk("d:/Solutions/PythonTraining/"):
    print( "Current Path:", dirpath)
    print("Directories:", dirnames)
    print("Files", fileames)
    print()

#environment
file_path = os.environ.get("Desktop")
print(file_path)
file_path = "d:/Solutions/PythonTraining/main_dir/sub_dir/demo.txt"
print(os.path.basename(file_path))
print(os.path.dirname(file_path))
print(os.path.split(file_path))
print(os.path.exists(file_path))
print(os.path.isdir(file_path))
print(os.path.isfile(file_path))
print(os.path.splitext(file_path))
print(dir(os.path))
'''
clear
& "D:/Program Files/Python39/python.exe" d:/Solutions/PythonTraining/08-os_module/app.py
'''