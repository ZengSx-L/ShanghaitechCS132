# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/Account.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(745, 495)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 100, 131, 131))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("uis\\image/头像.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(250, 100, 151, 51))
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 330, 601, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Bought_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Bought_btn.setObjectName("Bought_btn")
        self.gridLayout.addWidget(self.Bought_btn, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("uis\\image/我发布的.png"))
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.Sold_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Sold_btn.setObjectName("Sold_btn")
        self.gridLayout.addWidget(self.Sold_btn, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("uis\\image/我卖出的.png"))
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 1, 1, 1)
        self.Recharge_btn = QtWidgets.QPushButton(Form)
        self.Recharge_btn.setGeometry(QtCore.QRect(430, 180, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Recharge_btn.setFont(font)
        self.Recharge_btn.setObjectName("Recharge_btn")
        self.Back_btn = QtWidgets.QPushButton(Form)
        self.Back_btn.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.Back_btn.setObjectName("Back_btn")
        self.Logoff = QtWidgets.QPushButton(Form)
        self.Logoff.setGeometry(QtCore.QRect(430, 100, 131, 31))
        self.Logoff.setObjectName("Logoff")
        self.balance = QtWidgets.QLabel(Form)
        self.balance.setGeometry(QtCore.QRect(250, 180, 161, 51))
        self.balance.setObjectName("balance")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Myaccount"))
        self.label_2.setText(_translate("Form", "用户名：xxx"))
        self.Bought_btn.setText(_translate("Form", "我买到的"))
        self.Sold_btn.setText(_translate("Form", "我卖出的"))
        self.Recharge_btn.setText(_translate("Form", "充值！"))
        self.Back_btn.setText(_translate("Form", "返回主页"))
        self.Logoff.setText(_translate("Form", "登出"))
        self.balance.setText(_translate("Form", "余额：xxxx"))
