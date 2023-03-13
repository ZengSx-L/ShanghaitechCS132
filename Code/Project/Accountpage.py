from PyQt5.QtWidgets import QApplication, QInputDialog, QWidget, QPushButton, QMessageBox
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from pys.Account_UI import Ui_Form
from SqlTrade import MySQL_Trade
import sys
import globalData as gl
class Accountpage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.Back_btn.clicked.connect(self.back_to_main)
        self.ui.Bought_btn.clicked.connect(self.bought)
        self.ui.Sold_btn.clicked.connect(self.sold)
        self.ui.Recharge_btn.clicked.connect(self.recharge)
        self.ui.Logoff.clicked.connect(self.logoff)
        self.ui.label.setPixmap(QPixmap("uis/image/头像.jpg"))
        self.ui.label_7.setPixmap(QPixmap("uis/image/我发布的.png"))
        self.ui.label_8.setPixmap(QPixmap("uis/image/我卖出的.png"))

        self.query = MySQL_Trade()
        self.ui.retranslateUi(self)
        username = gl.get_value("user_name")
        balance = self.query.get_balance(gl.get_value("user_id"))
        if username != None:
            self.ui.label_2.setText("用户名:"+username)
        else:
            self.ui.label_2.setText("找不到用户名")
            
        self.ui.balance.setText("余额:"+str(balance))

    def sold(self):
        import ManageProducts
        self.deleteLater()
        self.cams = ManageProducts.ManageProd()
        self.cams.show()
    
    def bought(self):
        import Boughthistory
        self.deleteLater()
        self.cams = Boughthistory.Boughtpage()
        self.cams.show()

    def recharge(self):
        '''import Rechargepage
        self.deleteLater()
        self.cams = Rechargepage.Rechargepage()
        self.cams.show()'''
        usr = gl.get_value("user_id")
        origin = float(self.query.get_balance(usr))
        d,okPressed = QInputDialog.getDouble(self,"输入充值金额","金额：",100,0,999999.99,2)
        if okPressed:
            d = float(d)
            if(d + origin) > 999999.99:
                QtWidgets.QMessageBox().critical(self, "Error", "充值金额超上限",
                                                 QtWidgets.QMessageBox().Ok)
            else:
                t = d + origin
                self.query.set_balance(usr, t)
                #print(self.query.get_balance(usr))
        balance = self.query.get_balance(gl.get_value("user_id"))
        self.ui.balance.setText("余额:"+str(balance))

    def logoff(self):
        import LogSgn
        msg = QMessageBox.question(self, '提示', '是否登出？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if msg == QMessageBox.Yes:
            self.query.close_connect()
            self.deleteLater()
            self.cams = LogSgn.LoginWindow()
            self.cams.show()
        else:
            pass

    def back_to_main(self):
        import Mainpage
        self.query.close_connect()
        self.deleteLater()
        self.cams = Mainpage.Mainpage()
        self.cams.show()

import sys
if __name__ == '__main__':
    gl._init()
    gl.set_value("user_id",4)
    app = QApplication(sys.argv)
    window = Accountpage()
    window.show()
    app.exec()