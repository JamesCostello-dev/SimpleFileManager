#!/usr/bin/python3
# import modules
import os
# write a function to delete a file


def delete_file(filename):
    # get file name from user
    print('----------------------------------------------------')
    filename = input("Enter file name to delete: ")
    # check if the file exists
    if os.path.isfile(filename):
        # delete the file
        os.remove(filename)
        print('----------------------------------------------------')
        print("File deleted: " + filename)
    else:
        print('----------------------------------------------------')
        print("File not found: " + filename)
