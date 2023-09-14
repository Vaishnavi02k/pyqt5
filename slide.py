from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel,QTextEdit,QPushButton, QWidget,QSlider
from PyQt5 import QtCore, uic
import sys
#vertical and horizontal sliders are same
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #load the ui file
        uic.loadUi("slide.ui", self)
        self.setWindowTitle("Slider")

        #define Widgets
        self.label = self.findChild(QLabel,"label")
        self.slider = self.findChild(QSlider,"horizontalSlider")

        #centre label
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        

        #set slider properties
        self.slider.setRange(0,50)

        #move the slider and we are calling the function slide_it
        self.slider.valueChanged.connect(self.slide_it)
        self.slider.setValue(20)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(5)
        self.slider.setSingleStep(2)
      
        #show the app
        self.show()

    def slide_it(self,value):
        #grab the value from slider which can we directly get
        #pass that value to label and chnage the label
        self.label.setText(str(value))


#Initalize the app 
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()