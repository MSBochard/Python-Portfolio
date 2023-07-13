'''
Algorithm:  Uses regex to find all instances of numeric values within a text
            file. The numeric values can be of any length. Returns the number
            of numeric values found and their sum.
'''
#Imports the regex library
import re

#Opens the text file containing the numbers to find
fhand = open('py4e-data.dr-chuck.net_regex_sum_1762332.txt')

#Parses through the file, using regex to add all numeric values into a list
numList = []
for line in fhand:
    line = line.strip()
    num = re.findall('([0-9]+)', line)
    if len(num) > 0:
        for item in num:
            numList.append(int(item))

#Finds and returns the number of values and their sum
count = len(numList)
numSum = sum(numList)

print('There are', count, 'values with a sum of', numSum)
