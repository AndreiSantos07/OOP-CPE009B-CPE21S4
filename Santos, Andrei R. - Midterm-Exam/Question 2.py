import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):
    def __init__(self):
        super().__init__() #initializes the main window like in the previous one
        # window = QMainWindow
        self.title = "Special Midterm Exam in OOP"
        self.x = 300 # or left
        self.y = 300 # or top
        self.width = 400
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))

        #in GUI Python, these buttons, textboxes, labels are called widgets
        self.button = QPushButton('Click to Change Color', self)
        self.button.setToolTip("You've hovered over me!")
        self.button.move(150,120) #button.move(x,y)
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        self.button.setStyleSheet("background-color: yellow")
        print("Wow! The button becomes yellow :o")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
