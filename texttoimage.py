from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel,QTextEdit,QPushButton, QWidget, QLineEdit
from PyQt5 import QtCore, uic
from PyQt5.QtGui import QPixmap
import sys
from PIL import Image, ImageFont,ImageDraw 

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #load the ui file
        uic.loadUi("texttoimage.ui", self)
        self.setWindowTitle("Card")

        #define Widgets
        self.label = self.findChild(QLabel,"label")
        self.button = self.findChild(QPushButton,"pushButton")
        self.edit = self.findChild(QLineEdit,"lineEdit")

        #action to be taken when button is clicked
        self.button.clicked.connect(self.addText)

        #show the app
        self.show()

    def addText(self):
        #Grab the text
        myText = self.edit.text()

        #open the Image
        myImage =  Image.open("D:\PyQt5 Project\image.jpg")
        #define the font
        textFont = ImageFont.truetype("arial.ttf", 46)
        #Edit the image
        editImage = ImageDraw.Draw(myImage)
        editImage.text((80,400),myText,("black"),font=textFont)
        #save the Image
        myImage.save("D:\PyQt5 Project\image2.jpg")
        #Update our image
        pixmap = QPixmap("D:\PyQt5 Project\image2.jpg")
        self.label.setPixmap(pixmap)

        self.edit.setText("")

#Initalize the app 
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()