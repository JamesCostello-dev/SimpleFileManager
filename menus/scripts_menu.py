#!/usr/bin/python3

# import modules
import sys
import menus.main_menu as main_menu

# import scripts
from scripts.random_file import generate_shell_script

# fn for scripts menu
def scripts_menu():
    print('----------------------------------------------------')
    print("""
    ----------------------------------------------------
    |                                                    |
    |  1. Generate random file to desktop.               |
    |  2. Main menu.                                          |
    |  3. Exit.                                          |
    |                                                    |
    ----------------------------------------------------
    """)
    # get user input
    print('----------------------------------------------------')
    choice = input("Enter choice: ")
    # if user input is 1
    if choice == "1":
        # call path_finder fn
        generate_shell_script()
    # if user input is 2
    elif choice == "2":
        main_menu.main_menu()
    elif choice == "3":
        sys.exit()
    # if user input is invalid
    else:
        # print error message
        print('----------------------------------------------------')
        print("Invalid input.")
        # call scripts_menu fn
        scripts_menu()