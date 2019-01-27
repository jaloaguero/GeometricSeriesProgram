


from tkinter import *

master = Tk()

output = Label(master,text = "please enter pattern numbers seperated by spaces")
output.pack()

UserInput = Entry(master)
UserInput.pack()

def setToArray(UI):
    content = UserInput.get()
    print(content)


UserInput.bind('<Return>', setToArray)

master.mainloop()