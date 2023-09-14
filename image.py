from PyQt5.QtWidgets import QMainWindow,QPushButton, QApplication, QLabel, QFileDialog
from PyQt5 import uic
import sys
from PyQt5.QtGui import QPixmap

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        #load ui file
        uic.loadUi("image.ui",self)

        #define our widgets
        self.button = self.findChild(QPushButton,"pushButton")
        self.label = self.findChild(QLabel,"label")

        #connecting to the clicker function 
        self.button.clicked.connect(self.clicker)
        
        #show app
        self.show()

    def clicker(self):
        fname = QFileDialog.getOpenFileName(self,"Open File","E:\\vid & img\\Pins","All Files(*);; Jpg Files(*.jpg)")

        #open the image
        self.pixmap = QPixmap(fname[0])
        #add pic to label
        self.label.setPixmap(self.pixmap)

#initialize the app
app = QApplication(sys.argv)
UIWindow=UI()
app.exec_()