"""
Note: initially inside 'files' folder put some different types of files. then run this code
"""
import os # file operations
import shutil # copy and move operation in computer

path = input("Enter the path, which is unorganized: ")
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]
    print(filename, extension)

    if os.path.exists(path+"/"+extension):
        shutil.move(path+"/"+file, path+"/"+extension)+"/"+file
    else:
        os.makedirs(path+"/"+extension)
        shutil.move(path+"/"+file, path+"/"+extension+"/"+file)

print(files)
