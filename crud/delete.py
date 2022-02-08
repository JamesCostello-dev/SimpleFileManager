#!/usr/bin/python3
# import modules
import os
# write a function to delete a file


def delete_file(path_and_filename):
    # get user file path + file name
    print('----------------------------------------------------')
    path_and_filename = input("Enter path to file including file name: ")
    # check if the file exists
    if os.path.isfile(path_and_filename):
        # delete the file
        os.remove(path_and_filename)
        print('----------------------------------------------------')
        print("File deleted: " + path_and_filename)
    else:
        print('----------------------------------------------------')
        print("File not found: " + path_and_filename)
