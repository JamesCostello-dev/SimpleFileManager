#!/usr/bin/python3
# import modules
import os
# write a function to delete a file


def delete_file(filename):
    # get file name from user
    filename = input("Enter file name to delete: ")
    # check if the file exists
    if os.path.isfile(filename):
        # delete the file
        os.remove(filename)
        print("File deleted: " + filename)
    else:
        print("File not found: " + filename)
