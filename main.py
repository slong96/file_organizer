# file organizer

import os
import shutil

# checking if path exists
while True:
    path = input("Enter path (/User/John/Example): ")

    if os.path.exists(path):
        break
    else:
        print("Path not found. Please enter a valid path.")

files = os.listdir(path) # consist of list of files

"""
for loop to travel through every file,
split the file name and extension of the files.
"""
for file in files:
    filename, extension = os.path.splitext(file)
    # only need the extension name, removing the dot with slicing.
    extension = extension[1:]
    
    """
    if the extension folder (mp3, jpeg, zip, etc) exist,
    move the file to that folder

    else, make new folder and then move the file into it.
    """
    if os.path.exists(f'{path}/{extension}'):
        shutil.move(f'{path}/{file}', f'{path}/{extension}/{file}')
    else:
        os.makedirs(f'{path}/{extension}')
        shutil.move(f'{path}/{file}', f'{path}/{extension}/{file}')
    
print(f'Files in {path} are now organized.')
