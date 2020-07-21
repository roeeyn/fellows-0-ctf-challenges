#!python3
import os


# NOTE: put this to listen on port 9032

recipe = input("Which recipe do you wanna get? ")

os.system("cat ./recipes/" + recipe + ".txt")


