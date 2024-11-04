from tkinter import *

class MyWindow:
    def __init__(self, win):

        # common widgets
        self.Label1 = Label(win, fg="Red", text="Enter your fullname: ")
        self.Label1.place(x=30, y=80)

        self.Entry1 = Entry(win, bd=5)
        self.Entry1.place(x=220, y=80)

        self.Button1 = Button(win, bg="White", fg="Red", text = "Click to display your Fullname", command=self.show_name)
        self.Button1.place(x=30,y = 120)

        self.Entry2 = Entry(win, bd=5)
        self.Entry2.place(x=220, y=120)

    def show_name(self):
        result = self.Entry1.get()
        self.Entry2.insert(END, str(result))

window = Tk()
MyWin = MyWindow(window)

window.geometry("400x300+10+10")
window.title("Midterm in OOP")
window.mainloop()
