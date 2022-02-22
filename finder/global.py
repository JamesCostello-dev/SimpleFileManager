#!/usr/bin/python3

#import modules
import sys

# fn to get the input
def get_input():
    pattern = input("Enter the pattern to search: ")
    file = input("Enter the file name: ")
    return pattern, file

# fn to search for pattern in each file
def search_pattern(pattern, file):
    try:
        with open(file, 'r') as f:
            for line in f:
                if pattern in line:
                    print(line, end='')
    except FileNotFoundError:
        # print file not found error and request for another file
        print("File not found.\nPlease enter another file name.")
        file = input("Enter another file name:")
        search_pattern(pattern, file)

if __name__ == '__main__':
    pattern, file = get_input()
    search_pattern(pattern, file)
