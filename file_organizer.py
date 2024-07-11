import os
import shutil

def file_organize():
    # Checking if path exists
    while True:
        path = input("Enter path (User/John/Example) or (User\John\Example): ")

        if os.path.exists(path):
            break
        else:
            print("Path not found. Please enter a valid path.")

    files = os.listdir(path)  # Consist of list of files
    index = 0

    # For loop to travel through every file, split the file name and extension of the files.
    for file in files:
        filename, extension = os.path.splitext(file)
        # Only need the extension name, removing the dot with slicing.
        extension = extension[1:]
        
        # Ignore directories
        if os.path.isdir(os.path.join(path, file)):
            continue

        try:
            # If the extension folder (mp3, jpeg, zip, etc) exist, move the file to that folder
            # Else, make new folder and then move the file into it.
            if os.path.exists(f'{path}/{extension}'):
                shutil.move(f'{path}/{file}', f'{path}/{extension}/{file}')

            else:
                os.makedirs(f'{path}/{extension}')
                print(f"The '{extension}' folder has been created.")

                shutil.move(f'{path}/{file}', f'{path}/{extension}/{file}')

            index+=1
            print(f"{index}: '{file}' has been moved to the '{extension}' folder.")

        except PermissionError as e:
            print(f"Could not move {file}. Reason: {e}")
        except Exception as e:
            print(f"An error occurred with {file}. Reason: {e}")

file_organize()

# Prompt to close the program
input("Enter any key to close the program: ")