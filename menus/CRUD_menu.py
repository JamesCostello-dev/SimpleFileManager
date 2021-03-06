#!/usr/bin/python3

#import modules
import sys
import menus.main_menu as main_menu

# import CRUD modules
from crud.create import create_file
from crud.read import read_file
from crud.update import update_file
from crud.delete import delete_file

# function that gives the user a menu with options from CRUD
def crud_menu():
    print('----------------------------------------------------')
    print("""
    ----------------------------------------------------
    |                                                    |
    |  1. Create file.                                   |
    |  2. Read file.                                     |
    |  3. Update file.                                   |
    |  4. Delete file.                                   |
    |  5. Main menu.                                     |
    |  6. Exit.                                          |
    ----------------------------------------------------
    """)
    print('----------------------------------------------------')
    choice = input("Please enter your choice: ")
    if choice == "1":
        create_file()
    elif choice == "2":
        read_file()
    elif choice == "3":
        update_file(filename=None, filetext=None)
    elif choice == "4":
        delete_file(path_and_filename=None)
    elif choice == "5":
        main_menu.main_menu()
    elif choice == "6":
        sys.exit()
    else:
        print('----------------------------------------------------')
        print("Invalid choice.")
        crud_menu()