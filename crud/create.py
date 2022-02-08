#!/usr/bin/python3

# imports
import os

# write a function that reads a file
# and writes the file to a user selected path
# user input file name and text
# user input path

def create_file():
    # get user input for path
    path = input("Enter path: ")
    # get user input for file name
    filename = input("Enter filename: ")
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