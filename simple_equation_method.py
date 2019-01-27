#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#
# solves all equations with one instance of x^n

# imports math library
import math

__author__ = "mia"
__date__ = "$Jan 25, 2019 12:53:39 AM$"

# file variable reads testfile
file = open("testfile", "r")

# initialized empty array content
content = []

# for loop to read all elements from the file as float
for val in file.read().split():
    # takes file elements and saves into array content
    content.append(float(val))

# closes file
file.close()

# y_int variable for y intercept of the equation
# intercept is found where x = 0 (array[0] = y_int)
y_int = content[0]

# for loop to subtract y intercept from all elements of the array
for x in range(len(content)):
    content[x] -= y_int

# coefficient will equal content[1]
coefficient = content[1]

# now divide all elements of the array by the coefficient
for x in range(len(content)):
    content[x] = float(content[x] / coefficient)

# temp variable is initialized to the logbase2(content[2])
temp = math.log(content[2], 2)
# i variable is initialized to 1
# i will be used to find the denominator
i = 1
# power variable will hold the exponent
power = temp

# while the (temp * i) rounded to 2 decimal places
# is not an integer, then increment i, power now holds temp * i
while not round(temp * i, 2).is_integer():
    i += 1
    power = temp * i

# checks the coefficient
# when coefficient == 1
if coefficient == 1:
    print("y = " + "x", end = "")
# when coefficient == -1
elif coefficient == -1:
    print("y = -" + "x", end = "")
# when coefficient is an integer
elif coefficient.is_integer():
    print("y = " + str(int(coefficient)) + "x", end = "")
# when coefficient is not an integer
else:
    print("y = " + str(coefficient) + "x", end = "")

# checks the exponent (aka power)
# when the power == 1
if power == 1:
    print(" ", end = "")
# when the power is an integer
elif power.is_integer():
    print("^" + str(int(power)) + " ", end = "")
# when the power is not an integer
else:
    print("^(" + str(int(round(power, 2))) + "/" + str(i) + ") ", end = "")

# checks the y intercept
# when y int == 0
if y_int == 0:
    print()
# when y int < 0 and is an integer
elif y_int < 0 & y_int.is_integer():
    print("- " + str(int(-1 * y_int)))
# when y int < 0 and is not an integer
elif y_int < 0 & (not y_int.is_integer()):
    print("- " + str(-1 * y_int))
# when y > 0 and is an integer
elif y_int.is_integer():
    print("+ " + str(int(y_int)))
# when y > 0 and is not an integer
else:
    print("+ " + str(y_int))

# final equation has format y = mx^n + b
