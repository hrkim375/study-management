# main.py

from tkinter import *

class Main(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.width = master.winfo_screenwidth()
        self.height = master.winfo_screenheight()
        
        self.pack()
        self.createWidgets()

    def createWidgets(self):

        # menu1 Study Time
        self.menu1 = Button(self, text="1. Input your study time", width=self.width, height=2)
        self.menu1.pack(side="top")

        # menu2 Schedule
        self.menu2 = Button(self, text="2. Study schedule management", width=self.width, height=2)
        self.menu2.pack(side="top")
        
        # menu3 Status
        self.menu3 = Button(self, text="3. Print study status", width=self.width, height=2)
        self.menu3.pack(side="top")

root = Tk()
root.title("Study Management")
root.geometry("300x150")
root.resizable(width=False, height=False)
main = Main(master=root)
main.mainloop()
