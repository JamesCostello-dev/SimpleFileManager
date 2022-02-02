#!/usr/bin/python3

# import modules
import sys

# import fn from CRUD_menu.py
from menus.CRUD_menu import crud_menu
from menus.finder_menu import finder_menu
from menus.scripts_menu import scripts_menu

# main_menu fn for different menu options


def main_menu():
    print("""
    ----------------------------------------------------
    |                                                    |
    |  1. CRUD menu.                                     |
    |  2. Finder menu.                                   |
    |  3. Scripts menu.                                  |
    |  4. Exit.                                          |
    ----------------------------------------------------
    """)
    print('----------------------------------------------------')
    choice = input("Please enter your choice: ")
    if choice == "1":
        crud_menu()
    elif choice == "2":
        finder_menu()
    elif choice == "3":
        scripts_menu()
    elif choice == "4":
        sys.exit()
    else:
        print('----------------------------------------------------')
        print("Invalid choice.")
        main_menu()
