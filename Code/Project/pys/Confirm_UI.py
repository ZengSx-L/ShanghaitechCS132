# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/buyconfirm.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(439, 204)
        self.buyamount = QtWidgets.QLineEdit(Dialog)
        self.buyamount.setGeometry(QtCore.QRect(40, 40, 113, 20))
        self.buyamount.setObjectName("buyamount")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 54, 12))
        self.label.setObjectName("label")
        self.address = QtWidgets.QTextEdit(Dialog)
        self.address.setGeometry(QtCore.QRect(40, 100, 191, 31))
        self.address.setObjectName("address")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 54, 12))
        self.label_2.setObjectName("label_2")
        self.ok = QtWidgets.QPushButton(Dialog)
        self.ok.setGeometry(QtCore.QRect(230, 160, 80, 20))
        self.ok.setObjectName("ok")
        self.cancel = QtWidgets.QPushButton(Dialog)
        self.cancel.setGeometry(QtCore.QRect(330, 160, 80, 20))
        self.cancel.setObjectName("cancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "购买数量"))
        self.label_2.setText(_translate("Dialog", "收货地址"))
        self.ok.setText(_translate("Dialog", "确认"))
        self.cancel.setText(_translate("Dialog", "取消"))
