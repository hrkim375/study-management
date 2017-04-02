# __init__.py

from tkinter import *

class Time(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.width = 5

        self.pack()
        self.createWidgets()

    def createWidgets(self):

        # title label
        self.titleLabel = Label(self, text="Study Time")
        self.titleLabel.grid(row=0, column=1)

        # text field to input study time
        self.hourField = Entry(self, width=self.width)
        self.label = Label(self, text=":")
        self.minuteField = Entry(self, width=self.width)

        self.hourField.grid(row=1, column=0)
        self.label.grid(row=1, column=1)
        self.minuteField.grid(row=1, column=2)

        # input button
        self.button = Button(self, text="Input study time")
        self.button.grid(row=2, column=1)

root = Tk()
root.title("Study Time")
root.resizable(width=False, height=False)
app = Time(root)
app.mainloop()
