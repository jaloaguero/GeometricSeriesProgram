from tkinter import *

file = open("UserNumber", "w+")

master = Tk()

output = Label(master,text = "please enter pattern numbers seperated by spaces")
output.pack()

UserInput = Entry(master)
UserInput.pack()

def setToArray(UI):
    UINum = UserInput.get()
    #print(UINum)
    file.write(UINum)




UserInput.bind('<Return>', setToArray)

master.mainloop()

file.close()

#===============================================

__author__ = "mia"
__date__ = "$Jan 25, 2019 12:53:39 AM$"

# file variable reads testfile
file = open("UserNumber", "r")

# initialized empty array content
content = []

# for loop to read all elements as int
for val in file.read().split():
    content.append(float(val))

# closes file
file.close()

# y_int variable for y intercept of the equation
# intercept is found where x = 0 (array[0] = y_int
y_int = 1
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

# CHECK IF CONTENT[2] IS NOT AN INTEGER
# EXPONENT WILL BE NEGATIVE

# flag variable holds t/f if content[2] is an integer
flag: bool = (content[2]).is_integer()
# temp holds content[2]
temp = content[2]
# variable denominator created
denominator = 1
# variable numerator created
numerator = 0

# if exponent is not whole # or is < 0

power = 0

if not flag:
    # exponent is negative
    if content[2] < 1:
        content[2] = float(1 / content[2])
        power = -1
        print("power = " + str(power))

    temp = content[2]

    # if exponent is not a whole number
    while not temp.is_integer():
        temp = temp * content[2]
        denominator += 1
        print("temp = " + str(temp) + " d =" + str(denominator))

# finding numerator
while not temp == 1:
    temp = temp / 2
    numerator += 1

print("numerator = " + str(numerator))

power *= numerator

print("The exponent is " + str(power))

print("Final equation y = " + str(coefficient) + "x")