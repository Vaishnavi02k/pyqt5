# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect2_new.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(800, 224)
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 741, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.hide_main = QtWidgets.QPushButton(self.centralwidget)
        self.hide_main.setGeometry(QtCore.QRect(20, 100, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.hide_main.setFont(font)
        self.hide_main.setObjectName("hide_main")
        self.show_main = QtWidgets.QPushButton(self.centralwidget)
        self.show_main.setGeometry(QtCore.QRect(280, 100, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.show_main.setFont(font)
        self.show_main.setObjectName("show_main")
        self.hide_this = QtWidgets.QPushButton(self.centralwidget)
        self.hide_this.setGeometry(QtCore.QRect(540, 100, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.hide_this.setFont(font)
        self.hide_this.setObjectName("hide_this")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MainWindow"))
        self.label.setText(_translate("SecondWindow", "Type something"))
        self.hide_main.setText(_translate("SecondWindow", "Hide Main"))
        self.show_main.setText(_translate("SecondWindow", "Show Main"))
        self.hide_this.setText(_translate("SecondWindow", "Hide This one!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())