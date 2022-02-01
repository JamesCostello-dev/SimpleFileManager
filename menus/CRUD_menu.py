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
    print("""
    ----------------------------------------------------
    |                                                    |
    |  1. Create file.                                   |
    |  2. Read file.                                     |
    |  3. Update file.                                   |
    |  4. Delete file.                                   |
    |  5. Exit.                                          |
    ----------------------------------------------------
    """)
    print('----------------------------------------------------')
    choice = input("Please enter your choice: ")
    print('----------------------------------------------------')
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
        print('----------------------------------------------------')
        print("Invalid choice.")
        print('----------------------------------------------------')
        crud_menu()