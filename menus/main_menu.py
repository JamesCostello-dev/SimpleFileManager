#!/usr/bin/python3

# import modules
import sys

# import fn from CRUD_menu.py
from menus.CRUD_menu import crud_menu
from menus.finder_menu import finder_menu

# main_menu fn for different menu options
def main_menu():
    print("Please choose from the following options:")
    print("1. CRUD menu")
    print("2. Finder menu")
    print("3. Exit")
    choice = input("Please enter your choice: ")
    if choice == "1":
        crud_menu()
    elif choice == "2":
        finder_menu()
    elif choice == "3":
        sys.exit()
    else:
        print("Invalid choice.")
        main_menu()