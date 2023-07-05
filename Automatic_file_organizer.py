import os
import shutil

path = input("Enter the Path: ")

for file in os.listdir(path):
    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    destination_directory = os.path.join(path, extension)
    os.makedirs(destination_directory, exist_ok=True)

    source_path = os.path.join(path, file)
    destination_path = os.path.join(destination_directory, file)
    shutil.move(source_path, destination_path)
