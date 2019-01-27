#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# solves all equations with one instance of x^n

import math
from fractions import Fraction

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

# y_int variable for y intercept of the equation
# intercept is found where x = 0 (array[0] = y_int
y_int = content[0]

# prints out y intercept
print("The y intercept is " + str(y_int))

# for loop to subtract y intercept from all elements of the array
for x in range(len(content)):
    content[x] -= y_int

# @ content[1] = coefficient of x
coefficient = content[1]

# print out coefficient
print("The coefficient is " + str(coefficient))

# now divide all elements of the array by the coefficient
for x in range(len(content)):
    content[x] = float(content[x] / coefficient)

power = 0

power = math.log(content[2], 2)
i = 1
temp = power

while not round(power * i, 2).is_integer():
    i += 1
    temp = power * i

print(str(round(temp, 2)) + "/" + str(i))

# checks the coefficient
if coefficient == 1:
    print("y = " + "x", end = "")
elif coefficient == -1:
    print("y = -" + "x", end = "")
elif coefficient.is_integer():
    print("y = " + str(int(coefficient)) + "x", end = "")
else:
    print("y = " + str(coefficient) + "x", end = "")

# checks the exponent
if temp == 1:
    print(" ", end = "")
elif temp.is_integer():
    print("^" + str(int(temp)) + " ", end = "")
else:
    print("^(" + str(int(round(temp, 2))) + "/" + str(i) + ") ", end = "")

# checks the y intercept
if y_int == 0:
    print()
elif y_int < 0 & y_int.is_integer():
    print("- " + str(int(-1 * y_int)))
elif y_int < 0 & (not y_int.is_integer()):
    print("- " + str(-1 * y_int))
elif y_int.is_integer():
    print("+ " + str(int(y_int)))
else:
    print("+ " + str(y_int))

#
# print("testing testing")
#
# print("y = " + str(coefficient) + "x^(" + str(round(temp, 2)) + "/" + str(i) + ")" + " + " + str(y_int))