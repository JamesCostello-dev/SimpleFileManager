#!/usr/bin/python3

# import modules
import os

# fn to generate shell script
def generate_shell_script():
    # touch file in ~/Desktop/
    os.system("touch ~/Desktop/random_file.txt")
    # echo random text to the file
    os.system("echo 'Some random text' >> " + os.path.expanduser("~/Desktop/random_file.txt"))
    # print success message
    print("Successfully generated random_file.txt in ~/Desktop/")

if __name__ == "__main__":
    generate_shell_script()