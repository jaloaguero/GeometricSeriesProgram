#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#
# solves all equations with one instance of x^n

import math

from tkinter import *

# __author__ = "jalo"
# __date__ = "$Jan 26, 2019 - Jan 27, 2019"

# file variable writes to UserNumber
file = open("UserNumber", "w+")

# master is initialized as the Tk() class
master = Tk()

# output is initialized as Label, which prompts user to input 3 numbers and press Enter
output = Label(master, text = "Please enter 3 pattern numbers separated by spaces. "
                              "When you are done typing in your numbers, press Enter.")

# packs the widgets in a organized manner
output.pack()

# UserInput initialized as
UserInput = Entry(master)
UserInput.pack()

def setToArray(UI):
    UINum = UserInput.get()
    file.write(UINum)
    master.destroy()

UserInput.bind('<Return>', setToArray)

master.mainloop()

file.close()

#=================================================================

# __author__ = "mia"
# __date__ = "$Jan 26, 2019 - Jan 27, 2019"

# file variable reads UserNumber
file = open("UserNumber", "r")

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

teststr = ""

# checks the coefficient
# when coefficient == 1
if coefficient == 1:
    teststr += "y = x"
# when coefficient == -1
elif coefficient == -1:
    teststr += "y = -x"
# when coefficient is an integer
elif coefficient.is_integer():
    teststr += "y = " + str(int(coefficient)) + "x"
# when coefficient is not an integer
else:
    teststr += "y = " + str(coefficient) + "x"

# checks the exponent (aka power)
# when the power == 1
if power == 1:
    teststr += " "
# when the power is an integer
elif power.is_integer():
    teststr += "^" + str(int(power)) + " "
# when the power is not an integer
else:
    teststr += "^(" + str(int(round(power, 2))) + "/" + str(i) + ") "

# checks the y intercept
# when y int == 0
if y_int == 0:
    teststr += ""
# when y int < 0 and is an integer
elif y_int < 0 & y_int.is_integer():
    teststr += "- " + str(int(-1 * y_int))
# when y int < 0 and is not an integer
elif y_int < 0 & (not y_int.is_integer()):
    teststr += "- " + str(-1 * y_int)
# when y > 0 and is an integer
elif y_int.is_integer():
    teststr += "+ " + str(int(y_int))
# when y > 0 and is not an integer
else:
    teststr += "+ " + str(y_int)

# final equation has format y = mx^n + b

#========================================================================

next = Tk()

output = Label(next, text = "Final equation " + teststr)
output.pack()

output1 = Label(next, text = "Let's break this down")
output1.pack()

next.mainloop()

#========================================================================

# next1 = Tk()
#
# output = Label(next1, text = "To find the y intercept\n" + y_int)
# output.pack()
#
# next1.mainloop()
# next1.destroy()

print("fin")