#!/usr/bin/python3

# imports
import os

# write a function that reads a file
# and writes the file to a user selected path
# user input file name and text
# user input path

def create_file():
    # get user input for path, if path doesn't exist, create it
    path = input("Enter path: ")
    # loop and check if path exists
    while os.path.exists(path) == False:
        # if path doesn't exist, get user path again
        path = input("Path doesn't exist. Enter path: ")
    # get user input for file name
    filename = input("Enter filename: ")
    # check if file name exists
    while os.path.exists(path + "/" + filename) == True:
        # if file name exists, get user input again
        filename = input("File name exists. Enter filename: ")
    # get user input for text
    filetext = input("Enter text: ")
    # complete file path + filename
    complete_path = os.path.join(path, filename)
    # open file
    file = open(complete_path, "w")
    # write text to file
    file.write(filetext)
    # close file
    file.close()