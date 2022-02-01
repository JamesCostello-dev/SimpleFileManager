#!/usr/bin/python3

# import modoles
import sys

# import finder from fn
from finder.finder import path_finder

# finder_menu fn for different menu options
def finder_menu():
    print("""
    ----------------------------------------------------
    |                                                    |
    |  1. Path Finder.                                   |
    |  2. Exit.                                          |
    ----------------------------------------------------
    """)
    choice = input("Please enter your choice: ")
    if choice == "1":
        path_finder()
    elif choice == "2":
        sys.exit()
    else:
        print("Invalid choice.")
        finder_menu()