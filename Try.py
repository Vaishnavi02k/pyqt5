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
        my_label = qtw.QLabel("Hello, What's your name?")
        #Change the font size of label
        my_label.setFont(qtg.QFont('Helvetica',18))
        self.layout().addWidget(my_label)

        #Create an entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        #Create a button
        my_button= qtw.QPushButton("Press Me!",clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        #show the app
        self.show()

        def press_it():
            #Add name to lable
            my_label.setText(f'Hello {my_entry.text()}!')
            #clear the entry box
            my_entry.setText("")

        
app=qtw.QApplication([])
mw = MainWindow()

#Run The App
app.exec_()