#!/usr/bin/python3

# import modules
import os
from pathlib import Path


# write a function that finds a file in the file system
# and returns the path to the file
def finder():
    print("Please enter the name of the file you would like to find:")
    filename = input("Filename: ")
    # create a list of all files in the file system
    files = os.listdir()
    # loop through the list of files
    for file in files:
        # create a path object for each file
        path = Path(file)
        # if the filename matches the file in the file system
        if filename == path.name:
            # return the path to the file
            return path
    # if the file is not found
    print("File not found.")
    # return None
    return None