import typing
from PyQt5 import QtCore
import PyQt5.QtWidgets as qtw
from PyQt5.QtWidgets import QWidget
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #Add a Title
        self.setWindowTitle("Hello World!")
        
        #Set Vertical layout
        self.setLayout(qtw.QVBoxLayout())

        #Create A Label
        my_label = qtw.QLabel("Pick something from the list below")
        #Change the font size of label
        my_label.setFont(qtg.QFont('Helvetica',20))
        self.layout().addWidget(my_label)

        #Create an spin box
        my_spin = qtw.QSpinBox(self, value=10, maximum=100, minimum=0, singleStep=1, prefix="#", suffix=" Order")
        #Change size of spin box
        my_spin.setFont(qtg.QFont('Helvetica',16))
        #put combobox on the screen
        self.layout().addWidget(my_spin)


        #Create a button
        my_button= qtw.QPushButton("Press Me!",clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        #show the app
        self.show()

        def press_it():
            #Add name to lable
            my_label.setText(f'You Picked #{my_spin.value()} Order!')
            
        
app=qtw.QApplication([])
mw = MainWindow()

#Run The App
app.exec_()