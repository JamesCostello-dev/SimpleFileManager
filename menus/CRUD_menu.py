#!/usr/bin/python3

#import modules
import sys

# import CRUD modules
from crud.create import create_file
from crud.read import read_file
from crud.update import update_file
from crud.delete import delete_file

# function that gives the user a menu with options from CRUD
def crud_menu():
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
        crud_menu()