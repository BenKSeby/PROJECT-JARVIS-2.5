# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LOGIN(object):
    def setupUi(self, LOGIN):
        LOGIN.setObjectName("LOGIN")
        LOGIN.resize(451, 496)
        self.centralwidget = QtWidgets.QWidget(LOGIN)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 551, 601))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("login3.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 80, 371, 131))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.USERNAME = QtWidgets.QLineEdit(self.centralwidget)
        self.USERNAME.setGeometry(QtCore.QRect(190, 210, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.USERNAME.setFont(font)
        self.USERNAME.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);")
        self.USERNAME.setText("")
        self.USERNAME.setObjectName("USERNAME")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 210, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 270, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.PASSWORD = QtWidgets.QLineEdit(self.centralwidget)
        self.PASSWORD.setGeometry(QtCore.QRect(190, 270, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PASSWORD.setFont(font)
        self.PASSWORD.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.PASSWORD.setObjectName("PASSWORD")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(154, 372, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        LOGIN.setCentralWidget(self.centralwidget)

        self.retranslateUi(LOGIN)
        QtCore.QMetaObject.connectSlotsByName(LOGIN)

    def retranslateUi(self, LOGIN):
        _translate = QtCore.QCoreApplication.translate
        LOGIN.setWindowTitle(_translate("LOGIN", "MainWindow"))
        self.label_2.setText(_translate("LOGIN", "<html><head/><body><p><span style=\" color:#55ffff;\">LOGIN TO JARVIS</span></p></body></html>"))
        self.label_3.setText(_translate("LOGIN", "<html><head/><body><p><span style=\" color:#00aaff;\">USERNAME</span></p></body></html>"))
        self.label_4.setText(_translate("LOGIN", "<html><head/><body><p><span style=\" color:#00aa00;\">PASSWORD</span></p></body></html>"))
        self.pushButton.setText(_translate("LOGIN", "LOGIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LOGIN = QtWidgets.QMainWindow()
    ui = Ui_LOGIN()
    ui.setupUi(LOGIN)
    LOGIN.show()
    sys.exit(app.exec_())