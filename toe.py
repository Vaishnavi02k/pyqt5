from PyQt5.QtWidgets import QMainWindow,QPushButton, QApplication, QLabel, QFileDialog
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        #load ui file
        uic.loadUi("toe.ui",self)

        #Define A counter to keep Track of Who's Turn it is
        self.counter=0

        #define our widgets
        self.button1 = self.findChild(QPushButton,"pushButton_1")
        self.button2 = self.findChild(QPushButton,"pushButton_2")
        self.button3 = self.findChild(QPushButton,"pushButton_3")
        self.button4 = self.findChild(QPushButton,"pushButton_4")
        self.button5 = self.findChild(QPushButton,"pushButton_5")
        self.button6 = self.findChild(QPushButton,"pushButton_6")
        self.button7 = self.findChild(QPushButton,"pushButton_7")
        self.button8 = self.findChild(QPushButton,"pushButton_8")
        self.button9 = self.findChild(QPushButton,"pushButton_9")
        self.button10 = self.findChild(QPushButton,"start_over")
        self.label = self.findChild(QLabel,"label")

        #click the button
        self.button1.clicked.connect(lambda: self.clicker(self.button1))
        self.button2.clicked.connect(lambda: self.clicker(self.button2))
        self.button3.clicked.connect(lambda: self.clicker(self.button3))
        self.button4.clicked.connect(lambda: self.clicker(self.button4))
        self.button5.clicked.connect(lambda: self.clicker(self.button5))
        self.button6.clicked.connect(lambda: self.clicker(self.button6))
        self.button7.clicked.connect(lambda: self.clicker(self.button7))
        self.button8.clicked.connect(lambda: self.clicker(self.button8))
        self.button9.clicked.connect(lambda: self.clicker(self.button9))
        self.button10.clicked.connect(self.reset)

        #connecting to the clicker function 
        #self.button1.clicked.connect(self.clicker)
        
        #show app
        self.show()

    def checkWin(self):
        #Across
        if self.button1.text() != "" and self.button1.text() == self.button4.text() and self.button1.text() ==self.button7.text():
            self.win(self.button1, self.button4, self.button7)

        if self.button2.text() != "" and self.button2.text() == self.button5.text() and self.button2.text() ==self.button8.text():
            self.win(self.button2, self.button5, self.button8)

        if self.button3.text() != "" and self.button3.text() == self.button6.text() and self.button3.text() ==self.button9.text():
            self.win(self.button3, self.button6, self.button9)

        #Down
        if self.button1.text() != "" and self.button1.text() == self.button2.text() and self.button1.text() ==self.button3.text():
            self.win(self.button1, self.button2, self.button3)
        
        if self.button4.text() != "" and self.button4.text() == self.button5.text() and self.button4.text() ==self.button6.text():
            self.win(self.button4, self.button5, self.button6)
        
        if self.button7.text() != "" and self.button7.text() == self.button8.text() and self.button7.text() ==self.button9.text():
            self.win(self.button7, self.button8, self.button9)

        #Diagonal
        if self.button1.text() != "" and self.button1.text() == self.button5.text() and self.button1.text() ==self.button9.text():
            self.win(self.button1, self.button5, self.button9)
        
        if self.button3.text() != "" and self.button3.text() == self.button5.text() and self.button3.text() ==self.button7.text():
            self.win(self.button3, self.button5, self.button7)


    #defining win function here we are declaring the winner and making that letter to red and starting over
    def win(self,b1,b2,b3):
        #lets assume b1, b2, b3 are the buttons that we got after checking win
        #changing the color of that buttons to stand out
        b1.setStyleSheet('QPushButton {color: red;}')
        b2.setStyleSheet('QPushButton {color: red;}')
        b3.setStyleSheet('QPushButton {color: red;}')
        #Add winner label
        self.label.setText(f'{b1.text()} Wins!')

        #Disable the board 
        self.disable()
    
    def disable(self):
        button_list = [
            self.button1,            
            self.button2,            
            self.button3,            
            self.button4,            
            self.button5,            
            self.button6,            
            self.button7,            
            self.button8,            
            self.button9,
        ]
        #disable the buttons
        for b in button_list:
            b.setEnabled(False)
        
    #click the buttons
    def clicker(self,b):
        if self.counter % 2==0:
            mark = "X"
            self.label.setText("Its O's turn now")
        else:
            mark = "O"
            self.label.setText("Its X's turn now")
        b.setText(mark)
        b.setEnabled(False)
        #increment the counter
        self.counter += 1
        #Check if won
        self.checkWin()

    #start over
    def reset(self):
        #create the list of buttons
        button_list = [
            self.button1,            
            self.button2,            
            self.button3,            
            self.button4,            
            self.button5,            
            self.button6,            
            self.button7,            
            self.button8,            
            self.button9,
        ]
        #reset the buttons
        for b in button_list:
            b.setText("")
            b.setEnabled(True)
            #reset buttons color
            b.setStyleSheet('QPushButton {color: #797979;}')
        
        #reset the label
        self.label.setText("X's goes first!")

        #reset the counter
        self.counter = 0



    


#initialize the app
app = QApplication(sys.argv)
UIWindow=UI()
app.exec_()