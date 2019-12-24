# Author: Noah Wilson, wilsonn2018@my.fit.edu
# Course: CSE 2050, Fall 2019
# Project: ASCII Clock
"""The docstring for ASCII Clock"""

from sys import stdin, stdout


def output_stuff(check):
    """The function output_stuff takes a list as an input
       then prints out the numbers"""
    if check[0] == 2:
        stdout.write(" ")
    elif check[0] == 1:
        stdout.write("+")
    elif check[0] == 0:
        stdout.write("|")

    if check[1] == 0:
        stdout.write(" "*3)
    elif check[1] == 1:
        stdout.write("---")

    if check[2] == 2:
        stdout.write(" ")
    elif check[2] == 1:
        stdout.write("+")
    elif check[2] == 0:
        stdout.write("|")


TIMES = []

# First, I created a dictionary that contains a key for how to
# print out every number 0-9. The number will always be 5 spaces
# wide, and the three spaces in the middle of that 5 spaces
# will always be the same, which is why each array in the dictionary
# only has three numbers. The number will always be seven spaces
# in height so that is why there are seven lists for each number.
# List[0] and [2]: 2 = space, 1 = plus, 0 = vertical line
# List [1]: 0 = three spaces, 1 = three horizontal lines,
NUMBERS = {0: [[1, 1, 1], [0, 0, 0], [0, 0, 0], [1, 0, 1], [0, 0, 0],
               [0, 0, 0], [1, 1, 1]],
           1: [[2, 0, 1], [2, 0, 0], [2, 0, 0], [2, 0, 1], [2, 0, 0],
               [2, 0, 0], [2, 0, 1]],
           2: [[1, 1, 1], [2, 0, 0], [2, 0, 0], [1, 1, 1], [0, 0, 2],
               [0, 0, 2], [1, 1, 1]],
           3: [[1, 1, 1], [2, 0, 0], [2, 0, 0], [1, 1, 1], [2, 0, 0],
               [2, 0, 0], [1, 1, 1]],
           4: [[1, 0, 1], [0, 0, 0], [0, 0, 0], [1, 1, 1], [2, 0, 0],
               [2, 0, 0], [2, 0, 1]],
           5: [[1, 1, 1], [0, 0, 2], [0, 0, 2], [1, 1, 1], [2, 0, 0],
               [2, 0, 0], [1, 1, 1]],
           6: [[1, 1, 1], [0, 0, 2], [0, 0, 2], [1, 1, 1], [0, 0, 0],
               [0, 0, 0], [1, 1, 1]],
           7: [[1, 1, 1], [2, 0, 0], [2, 0, 0], [2, 0, 1], [2, 0, 0],
               [2, 0, 0], [2, 0, 1]],
           8: [[1, 1, 1], [0, 0, 0], [0, 0, 0], [1, 1, 1], [0, 0, 0],
               [0, 0, 0], [1, 1, 1]],
           9: [[1, 1, 1], [0, 0, 0], [0, 0, 0], [1, 1, 1], [2, 0, 0],
               [2, 0, 0], [1, 1, 1]]
          }


for line in stdin:
    input_s = line.split()
    # I store all the times in a list called TIMES
    for i in range(len(input_s)):
        if input_s[i] == "end":
            break
        else:
            TIMES.append(input_s[i])

# This for loop prints everything out. So starting from the beginning
# of the TIMES list, I take the time and assign it to the variable
# "number".
for r in range(len(TIMES)):
    number = TIMES[r]
    # In this for loop, I loop seven times because that is the height
    # of the outputted number. I create a new list, called "check_list"
    # which is assigned the list in the dictionary that corresponds
    # with that number in the time.
    for j in range(0, 7):
        check_list = NUMBERS[int(number[0])][j]
        output_stuff(check_list)
        stdout.write("  ")

        check_list = NUMBERS[int(number[1])][j]
        output_stuff(check_list)

        # At position 2 and 4, a colon needs to be inserted.
        if j == 2 or j == 4:
            stdout.write("  o  ")
        else:
            stdout.write(" "*5)

        check_list = NUMBERS[int(number[3])][j]
        output_stuff(check_list)
        stdout.write("  ")

        check_list = NUMBERS[int(number[4])][j]
        output_stuff(check_list)
        stdout.write("\n")
    stdout.write("\n")
    stdout.write("\n")
