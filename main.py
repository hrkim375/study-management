# main.py

# import tkinter module
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

        # Study Time
        self.studyTimeButton = Button(self, text="1. Input your study time", width=self.width, command=self.study_time)
        self.studyTimeButton.grid(row=1)

        # Schedule
        self.scheduleButton = Button(self, text="2. Study schedule management", width=self.width)
        self.scheduleButton.grid(row=2)
        
        # Status
        self.statusButton = Button(self, text="3. Print study status", width=self.width)
        self.statusButton.grid(row=3)

    def study_time(self):
        # import study_time module and run the module
        import study_time
        study_time.app()

root = Tk()
root.title("Study Management")
root.resizable(width=False, height=False)
main = Main(master=root)
main.mainloop()
