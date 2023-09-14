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
        my_label.setFont(qtg.QFont('Helvetica',24))
        self.layout().addWidget(my_label)

        #Create an combo box
        my_combo = qtw.QComboBox(self, editable=True, insertPolicy=qtw.QComboBox.InsertAtBottom)
        #add Items to the combo box
        my_combo.addItem("Pepperoni" , "something")
        my_combo.addItem("Cheese" ,2 )
        my_combo.addItem("Mushroom", qtw.QWidget)
        my_combo.addItem("Pepper")
        my_combo.addItems(["one","Two","Three"])
        my_combo.insertItem(2,"Third Thing")
        #put combobox on the screen
        self.layout().addWidget(my_combo)


        #Create a button
        my_button= qtw.QPushButton("Press Me!",clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        #show the app
        self.show()

        def press_it():
            #Add name to lable
            my_label.setText(f'You Picked {my_combo.currentText()}!')
            
        
app=qtw.QApplication([])
mw = MainWindow()

#Run The App
app.exec_()