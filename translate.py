from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel,QTextEdit,QPushButton, QWidget
from PyQt5 import QtCore, uic
import sys
#import googletrans
#import textblob

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #load the ui file
        uic.loadUi("translate.ui", self)
        self.setWindowTitle("Translator App")

        #define Widgets
        self.label = self.findChild(QLabel,"label")
        self.textedit = self.findChild(QTextEdit,"textEdit")
        self.button = self.findChild(QPushButton,"pushButton")
        self.clear_button = self.findChild(QPushButton,"clear_textbox")

        #Define functions
        self.button.clicked.connect(self.clicker)
        self.clear_button.clicked.connect(self.clearer)

        #show the app
        self.show()

    def clicker(self):
        self.label.setText(f'Hello There {self.textedit.toPlainText()}')
        self.textedit.setPlainText("")
    
    def clearer(self):
        self.textedit.setText("")
        self.label.setText("Enter your Name")


#Initalize the app 
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()