#!/usr/bin/python3

# import modules
import os

# fn to find absolute path of a file
def path_finder():
    # get file name
    file_name = input("Enter file name: ")a
    # search file system for file print result
    for root, dirs, files in os.walk("/Users/"):
        for file in files:
            if file == file_name:
                print('----------------------------------------------------')
                print(os.path.join(root, file))
                print('----------------------------------------------------')
                return
    # if file not found print error message
    print("File not found.")
    return
