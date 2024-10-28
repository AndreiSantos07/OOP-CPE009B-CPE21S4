import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QMenuBar, QAction, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class ScientificCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Scientific Calculator')
        self.setGeometry(300, 300, 400, 400)

        # Create a menu bar
        menubar = QMenuBar(self)
        fileMenu = menubar.addMenu('File')
        saveAction = QAction('Save', self)
        saveAction.triggered.connect(self.saveToFile)
        fileMenu.addAction(saveAction)
        loadAction = QAction('Load', self)
        loadAction.triggered.connect(self.loadFromFile)
        fileMenu.addAction(loadAction)
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        # Create a grid layout
        grid = QGridLayout()
        self.setLayout(grid)

        self.textLine = QLineEdit(self)
        grid.addWidget(self.textLine, 0, 0, 1, 4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sin', 'cos', 'exp', 'C'
        ]

        positions = [(i, j) for i in range(1, 6) for j in range(4)]

        for position, name in zip(positions, buttons):
            button = QPushButton(name)
            button.clicked.connect(self.on_click)
            grid.addWidget(button, *position)

        self.show()

    @pyqtSlot()
    def on_click(self):
        sender = self.sender()
        text = sender.text()

        if text == 'C':
            self.textLine.clear()
        elif text == '=':
            try:
                result = str(eval(self.textLine.text()))
                self.textLine.setText(result)
            except Exception as e:
                self.textLine.setText('Error')
        elif text in ['sin', 'cos', 'exp']:
            try:
                value = float(self.textLine.text())
                if text == 'sin':
                    result = str(math.sin(math.radians(value)))
                elif text == 'cos':
                    result = str(math.cos(math.radians(value)))
                elif text == 'exp':
                    result = str(math.exp(value))
                self.textLine.setText(result)
            except Exception as e:
                self.textLine.setText('Error')
        else:
            self.textLine.setText(self.textLine.text() + text)

    def saveToFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.textLine.text())

    def loadFromFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'r') as file:
                self.textLine.setText(file.read())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScientificCalculator()
    sys.exit(app.exec_())
