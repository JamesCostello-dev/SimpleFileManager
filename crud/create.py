#!/usr/bin/python3
# write a function that reads a file and prints it to the screen
def create_file():
    # ask user to enter a file name, then store it in a variable
    print('----------------------------------------------------')
    file_name = input("Please enter a file name: ")
    # open the file in write mode
    file_object = open(file_name, "w")
    # ask user to enter text, then store it in a variable
    print('----------------------------------------------------')
    file_text = input("Please enter text: ")
    # write the text to the file
    file_object.write(file_text)
    # close the file
    file_object.close()
