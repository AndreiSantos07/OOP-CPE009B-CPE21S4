from tkinter import *

class MyWindow:
    def __init__(self, win):

        win.config(bg = "Black")
        # common widgets
        self.Label1 = Label(win, bg="White", fg="Black", text="~Calculator~", font = ("Times New Roman", 12))
        self.Label1.place(x=150, y=50)

        self.Label2 = Label(win, fg="Dark Green", text="Number 1: ")
        self.Label2.place(x=50, y=80)

        self.Entry1 = Entry(win, bd=5)
        self.Entry1.place(x=150, y=80)

        self.Label3 = Label(win, fg="Dark Green", text="Number 2: ")
        self.Label3.place(x=50, y=120)

        self.Entry2 = Entry(win, bd=5)
        self.Entry2.place(x=150, y=120)

        self.Label4 = Label(win, fg="Dark Green", text="Result: ")
        self.Label4.place(x=50, y=160)

        self.Entry3 = Entry(win, bd=5)
        self.Entry3.place(x=150, y=160)

        self.Button1 = Button(win, bg="White", fg="Black", text = "Add", command=self.add)
        self.Button1.place(x=80,y = 200)

        self.Button2 = Button(win, bg="White", fg="Black", text = "Subtract", command=self.sub)
        self.Button2.place(x=120,y = 200)

        self.Button3 = Button(win, bg="White", fg="Black", text = "Multiply", command=self.mul)
        self.Button3.place(x=180,y = 200)

        self.Button4 = Button(win, bg="White", fg="Black", text = "Divide", command=self.div)
        self.Button4.place(x=240,y = 200)

        self.Button5 = Button(win, bg="White", fg="Black", text = "CA", command=self.CA)
        self.Button5.place(x=290,y = 200)
        self.Button5.bind('<Button-1>',self.CA)


    def add(self):
        self.Entry3.delete(0,'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 + num2
        self.Entry3.insert(END, str(result))

    def sub(self):
        self.Entry3.delete(0,'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 - num2
        self.Entry3.insert(END, str(result))

    def mul(self):
        self.Entry3.delete(0,'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 * num2
        self.Entry3.insert(END, str(result))

    def div(self):
        self.Entry3.delete(0,'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 / num2
        self.Entry3.insert(END, str(result))

    def CA(self):
        self.Entry1.delete(0,'end')
        self.Entry2.delete(0,'end')
        self.Entry3.delete(0,'end')

window = Tk()
MyWin = MyWindow(window)

window.geometry("400x300+10+10")
window.title("Standard Calculator")
window.mainloop()
