from Registration import MyWindow
from tkinter import Tk

window = Tk()
MyWin = MyWindow(window)
window.geometry("400x400+10+10")
window.title("Account Registration Form")
window.mainloop()
