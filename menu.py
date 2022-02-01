#!/usr/bin/python3

# import modules
import sys

# import functions
from create import create_file
from read import read_file
from update import update_file
from delete import delete_file


# function that gives the user a menu
# the menu allows the user to choose from the following options:

def menu():
    print("Please choose from the following options:")
    print("1. Create a file")
    print("2. Read a file")
    print("3. Update a file")
    print("4. Delete a file")
    print("5. Exit")
    choice = input("Please enter your choice: ")
    if choice == "1":
        create_file()
    elif choice == "2":
        read_file()
    elif choice == "3":
        update_file(filename=None, filetext=None)
    elif choice == "4":
        delete_file(filename=None)
    elif choice == "5":
        sys.exit()
    else:
        print("Invalid choice.")
        menu()
