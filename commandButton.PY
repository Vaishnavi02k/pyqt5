# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'commandButton.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.count = 0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(499, 104)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.next_commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget, clicked = lambda: self.increment())
        self.next_commandLinkButton.setGeometry(QtCore.QRect(10, 10, 222, 48))
        self.next_commandLinkButton.setDefault(False)
        self.next_commandLinkButton.setObjectName("next_commandLinkButton")
        self.next_label = QtWidgets.QLabel(self.centralwidget)
        self.next_label.setGeometry(QtCore.QRect(280, 10, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.next_label.setFont(font)
        self.next_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.next_label.setObjectName("next_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 499, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.next_commandLinkButton.setText(_translate("MainWindow", "Increase Counter"))
        self.next_label.setText(_translate("MainWindow", "0"))

    def increment(self):
        #increment in counter
        self.count+=1

        #output to the label
        self.next_label.setText(str(self.count))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
