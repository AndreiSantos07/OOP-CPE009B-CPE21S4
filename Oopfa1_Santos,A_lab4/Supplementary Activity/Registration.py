from tkinter import *
from tkinter import messagebox
class MyWindow:
    def __init__(self, win):

        win.config(bg = "Black")
        # common widgets
        self.Label1 = Label(win, bg="White", fg="Black", text="Account Registration System", font = ("Times New Roman", 12))
        self.Label1.place(x=110, y=20)

        self.Label2 = Label(win, fg="Dark Green", text="First Name: ")
        self.Label2.place(x=90, y=80)

        self.Entry1 = Entry(win, bd=1)
        self.Entry1.place(x=190, y=80)

        self.Label3 = Label(win, fg="Dark Green", text="Last Name: ")
        self.Label3.place(x=90, y=120)

        self.Entry2 = Entry(win, bd=1)
        self.Entry2.place(x=190, y=120)

        self.Label4 = Label(win, fg="Dark Green", text="Username: ")
        self.Label4.place(x=90, y=160)

        self.Entry3 = Entry(win, bd=1)
        self.Entry3.place(x=190, y=160)

        self.Label5 = Label(win, fg="Dark Green", text="Password: ")
        self.Label5.place(x=90, y=200)

        self.Entry4 = Entry(win, bd=1, show ='*')
        self.Entry4.place(x=190, y=200)

        self.Label6 = Label(win, fg="Dark Green", text="Email Address: ")
        self.Label6.place(x=90, y=240)

        self.Entry5 = Entry(win, bd=1)
        self.Entry5.place(x=190, y=240)

        self.Label7 = Label(win, fg="Dark Green", text="Contact No.: ")
        self.Label7.place(x=90, y=280)

        self.Entry6 = Entry(win, bd=1)
        self.Entry6.place(x=190, y=280)

        self.Button1 = Button(win, bg="White", fg="Black", text="Submit", command = self.submit)
        self.Button1.place(x=120, y=320)

        self.Button2 = Button(win, bg="White", fg="Black", text="Clear", command=self.clear)
        self.Button2.place(x=220, y=320)

    def clear(self):
        self.Entry1.delete(0,'end')
        self.Entry2.delete(0,'end')
        self.Entry3.delete(0,'end')
        self.Entry4.delete(0, 'end')
        self.Entry5.delete(0, 'end')
        self.Entry6.delete(0, 'end')

    def submit(self):
        messagebox.showinfo("Submitted Data", "Congratulations for filling the form!")

