#!/usr/bin/python3

# import modoles
import sys
import menus.main_menu as main_menu

# import finder from fn
from finder.finder import path_finder

# finder_menu fn for different menu options
def finder_menu():
    print("""
    ----------------------------------------------------
    |                                                    |
    |  1. Path finder.                                   |
    |  2. Main menu.                                          |
    |  2. Exit.                                          |
    ----------------------------------------------------
    """)
    print('----------------------------------------------------')
    choice = input("Please enter your choice: ")
    if choice == "1":
        path_finder()
    elif choice == "2":
        main_menu.main_menu()
    elif choice == "3":
        sys.exit()
    else:
        print('----------------------------------------------------')
        print("Invalid choice.")
        finder_menu()