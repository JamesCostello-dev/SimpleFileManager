#!/usr/bin/python3

# import modules
import os
import menus.finder_menu as finder_menu

# fn to find absolute path of a file


def path_finder():
    # get file name
    print('----------------------------------------------------')
    file_name = input("Enter file name: ")
    # search file system for file print result
    for root, dirs, files in os.walk("/Users/"):
        for file in files:
            # if file name matches
            if file == file_name:
                # print absolute path
                print('----------------------------------------------------')
                print("Path found: " + os.path.join(root, file))
                # call finder menu
                finder_menu.finder_menu()         
    # if file not found
    print('----------------------------------------------------')
    print("File not found.")
    # call finder menu
    finder_menu.finder_menu()      
