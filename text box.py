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
        my_label = qtw.QLabel("Type here:")
        #Change the font size of label
        my_label.setFont(qtg.QFont('Helvetica',20))
        self.layout().addWidget(my_label)

        #Create an text box
        my_text = qtw.QTextEdit(self,
            #plainText="This is real text!",
            #html="<centre> <h1><em>Big Header Text!</em></h1><centre>",
            acceptRichText=True,
            lineWrapMode=qtw.QTextEdit.FixedColumnWidth, lineWrapColumnOrWidth = 50, placeholderText="Hello World!", readOnly=False
        )
        #Change size of spin box
        #my_spin.setFont(qtg.QFont('Helvetica',16))
        #put combobox on the screen
        self.layout().addWidget(my_text)


        #Create a button
        my_button= qtw.QPushButton("Press Me!",clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        #show the app
        self.show()

        def press_it():
            #Add name to lable
            my_label.setText(f'You typed {my_text.toPlainText()}')
            my_text.setPlainText("You Pressed the Button!")
            
        
app=qtw.QApplication([])
mw = MainWindow()

#Run The App
app.exec_()