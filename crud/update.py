#!/usr/bin/python3

# import modules
import os

# update needed w/ file path
# write a function to update filetext and file name
def update_file(filename, filetext):
    # get file name from user
    print('----------------------------------------------------')
    filename = input("Enter file name to update: ")
    # check if the file exists
    if os.path.isfile(filename):
        # open the file
        f = open(filename, "w")
        # get file text from user
        print('----------------------------------------------------')
        filetext = input("Enter file text: ")
        # write the file text
        f.write(filetext)
        # ask user if they want to change the file name
        print('----------------------------------------------------')
        change_name = input("Do you want to change the file name? (y/n): ")
        # if yes, get the new file name
        if change_name == "y":
            print('----------------------------------------------------')
            new_filename = input("Enter new file name: ")
            # rename the file
            os.rename(filename, new_filename)
            print('----------------------------------------------------')
            print("File renamed: " + new_filename)
        # close the file
        f.close()