#!/usr/bin/python3

# import modules
import sys

# write a function that reads a file and prints it to the screen


def read_file():
    # ask user to enter a file name, then store it in a variable
    file_name = input("Please enter a file name: ")
    # open the file in read mode
    file_object = open(file_name, "r")
    # if file name is not found, print an error message
    if file_object == None:
        print("File not found.")
        # exit the program
        sys.exit()
    # read the file
    file_text = file_object.read()
    # print the file to the screen
    print('-----------------')
    print('-----------------')
    print('-----------------')
    print(file_text)
    print('-----------------')
    print('-----------------')
    print('-----------------')
    # close the file
    file_object.close()
