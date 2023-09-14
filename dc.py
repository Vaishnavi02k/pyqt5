import typing
from PyQt5.QtWidgets import QMainWindow,QPushButton, QApplication, QLabel, QComboBox,QWidget
from PyQt5 import QtCore, uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        #load ui file
        uic.loadUi("dc.ui",self)

        #define widgets
        self.gender_combo = self.findChild(QComboBox,"gender_combobox")
        self.name_combo = self.findChild(QComboBox,"name_combobox")
        self.label = self.findChild(QLabel,"label")

        #add items in combo box
        self.gender_combo.addItem("Male", ["Yuvraj","Atharva","Rushikesh","Harsh"])        
        self.gender_combo.addItem("Female", ["Vaishnavi","Pooja","Diya","Shreya"])        

        # click the first dropdown
        self.gender_combo.activated.connect(self.clicker)
        self.name_combo.activated.connect(self.clicker2)

        #show app
        self.show()

    def clicker(self,index):
        #clear the second box
        self.name_combo.clear()
        #do the dependant thing
        self.name_combo.addItems(self.gender_combo.itemData(index))

    def clicker2(self):
        self.label.setText(f'You Picked: {self.name_combo.currentText()} a {self.gender_combo.currentText()}')
#initialize the app
app = QApplication(sys.argv)
UIWindow=UI()
app.exec_()