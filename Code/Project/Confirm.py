import sys
import os
import shutil
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QInputDialog,QFileDialog,QDialog
from pys.Confirm_UI import Ui_Dialog
from SqlTrade import MySQL_Trade
import globalData as gl 

class ConfirmDia(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.cancel.clicked.connect(self.cancel)
        self.ui.ok.clicked.connect(self.ok)
        self.query = MySQL_Trade()
        amount_reg = QtCore.QRegExp('[1-9][0-9]{0,5}')
        validator = QtGui.QRegExpValidator(self)
        validator.setRegExp(amount_reg)
        self.ui.buyamount.setValidator(validator)

        curr = gl.get_value("curr_item")
        data = gl.get_value("item%d"%curr)
        #print(data)
        self.item_id = data[0]
        self.price =  float(data[2])
        self.seller = data[3]
        self.stock = data[4]
        #self.ui.Discription.setText(data[5])
        #self.ui.Pic.setPixmap(QPixmap("uis/image/"+data[6]))


        self.ui.retranslateUi(self)

    def cancel(self):
        self.accept()

    def ok(self):
        amount = int(self.ui.buyamount.text())
        address = self.ui.address.toPlainText()
        price = float(amount) * self.price
        buyer = gl.get_value("user_id")
        
        #item_id,seller_id,buyer_id,amount,price,address
        if amount > self.stock:
            QMessageBox().critical(self, "Error", "库存不足", QMessageBox().Ok)
            return
        if price > float(999999.99):
            QMessageBox().critical(self, "Error", "单次交易金额超上限(999999.99元)", QMessageBox().Ok)
            return
        if len(address) > 49:
            QMessageBox().warning(self, "Error", "地址字数超上限（50字）",QMessageBox().Ok)
            return
        data = [self.item_id,self.seller,buyer,amount,price,address]
        self.query.query_insert(data)
        #print(self.query.query_select_buyer(buyer))
        self.accept()