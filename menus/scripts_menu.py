#!/usr/bin/python3

# import scripts
from scripts.random_file import generate_shell_script

# fn for scripts menu
def scripts_menu():
    # print scripts menu
    print("""
    ----------------------------------------------------
    |                                                    |
    |  1. Generate random file to desktop.               |
    |  2. Exit.                                          |
    |                                                    |
    ----------------------------------------------------
    """)
    # get user input
    choice = input("Enter choice: ")
    # if user input is 1
    if choice == "1":
        # call path_finder fn
        generate_shell_script()
    # if user input is 2
    elif choice == "2":
        # exit
        exit()
    # if user input is invalid
    else:
        # print error message
        print("Invalid input.")
        # call scripts_menu fn
        scripts_menu()