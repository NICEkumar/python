# this is to illustrate file operations

import os.path
import sys


filename = input("Enter a file name:")

if not os.path.isfile(filename):
    print("Entered file does not exits..")
    sys.exit(0)

file = open(filename, 'r')
lineList = file.readlines()

n = int(input("Enter the number of lines to read:"))

for i in range(n):
    print(f"{i+1}  :  {lineList[i]}")

word = input("Enter the word to be checked:")

numberOfWords = 0

for i in lineList:
    numberOfWords += i.count(word)

print(f"The word {word} repeats {numberOfWords} times")