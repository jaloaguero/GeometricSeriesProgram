#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "mia"
__date__ = "$Jan 25, 2019 12:53:39 AM$"

# file variable reads testfile
file = open("testfile", "r")

# initialized empty array content
content = []

# for loop to read all elements as int
for val in file.read().split():
    content.append(float(val))

# closes file
file.close()

for x in range(len(content)):
    print(content[x])

# sorts file
content.sort()

print("The array has been sorted")

for x in range(len(content)):
    print(content[x])

# assuming array is sorted:

# y_int variable for y intercept of the equation
# intercept is found where x = 0 (array[0] = y_int
y_int = content[0]

# prints out y intercept
print("The y intercept is " + str(y_int))

# for loop to subtract y intercept from all elements of the array
for x in range(len(content)):
    content[x] -= y_int
    print(content[x])

# @ content[1] = coefficient of x
coefficient = content[1]

# print out coefficient
print("The coefficient is " + str(coefficient))

# now divide all elements of the array by the coefficient
for x in range(len(content)):
    content[x] = float(content[x] / coefficient)
    print(content[x])

# now find content[2]
temp = content[2]

# power variable
power = 0

# while loop to dividing content[2] by 2 until content[2] == 1
# to find exponent
while (content[2] != 1):
    content[2] = float(content[2] / 2)
    power += 1
    print(content[2])

print("The exponent is " + str(power))