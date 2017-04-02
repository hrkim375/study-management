# main.py

from tkinter import *

class Main(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.width = 30
        
        self.pack()
        self.createWidgets()

    def createWidgets(self):

        # menu Label
        self.menuLabel = Label(self, text="Menu")
        self.menuLabel.grid(row=0)

        # menu1 Study Time
        self.menu1 = Button(self, text="1. Input your study time", width=self.width)
        self.menu1.grid(row=1)

        # menu2 Schedule
        self.menu2 = Button(self, text="2. Study schedule management", width=self.width)
        self.menu2.grid(row=2)
        
        # menu3 Status
        self.menu3 = Button(self, text="3. Print study status", width=self.width)
        self.menu3.grid(row=3)

root = Tk()
root.title("Study Management")
root.resizable(width=False, height=False)
main = Main(master=root)
main.mainloop()
