from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt, QRect
from pys.Mainpage_UI import Ui_Form
import globalData as gl 
import LogSgn
from SqlItem import MySQL_Item
end = False
class Mainpage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.Log_Sgn_btn.clicked.connect(self.account)
        self.ui.Prod_manage_btn.clicked.connect(self.manage)

        self.ui.info_1_btn.clicked.connect(lambda:self.buypage(0))
        self.ui.info_2_btn.clicked.connect(lambda:self.buypage(1))
        self.ui.info_3_btn.clicked.connect(lambda:self.buypage(2))
        self.ui.info_4_btn.clicked.connect(lambda:self.buypage(3))

        self.query = MySQL_Item()

        if(gl.get_value("admin") == 1):
            self.ui.Manager_btn = QPushButton(self.ui.groupBox)
            self.ui.Manager_btn.setGeometry(QRect(0, 110, 149, 23))
            self.ui.Manager_btn.setText("交易管理")
            self.ui.Manager_btn.clicked.connect(self.managerpage)
        else:
            self.ui.Release_prod_btn = QPushButton(self.ui.groupBox)
            self.ui.Release_prod_btn.setGeometry(QRect(0, 110, 149, 23))
            self.ui.Release_prod_btn.setText("商品发布")
            self.ui.Release_prod_btn.clicked.connect(self.release)
            self.ui.Prod_bought_btn = QPushButton(self.ui.groupBox)
            self.ui.Prod_bought_btn.setGeometry(QRect(0, 150, 149, 23))
            self.ui.Prod_bought_btn.setText("已购商品")
            self.ui.Prod_bought_btn.clicked.connect(self.bought)
            self.ui.Prod_sold_btn = QPushButton(self.ui.groupBox)
            self.ui.Prod_sold_btn.setGeometry(QRect(0, 190, 149, 23))
            self.ui.Prod_sold_btn.setText("已售出商品")
            self.ui.Prod_sold_btn.clicked.connect(self.sold)

        self.ui.retranslateUi(self)
        self.ui.prev_page_btn.clicked.connect(self.prevpage)
        self.ui.next_page_btn.clicked.connect(self.nextpage)

        self.tag = -1
        self.ui.Tag1_btn.clicked.connect(lambda: self.settag(0))
        self.ui.Tag2_btn.clicked.connect(lambda: self.settag(1))
        self.ui.Tag3_btn.clicked.connect(lambda: self.settag(2))

        self.ui.Search_btn.clicked.connect(self.search)
        
        gl.set_value("page",0)
        self.find_item()
        self.show_page()

    def show_page(self):
        item = gl.get_value("item0")
        nopic = "uis/image/消息.png"
        if item:
            self.ui.name_1.setText(item[1])
            path = "uis/image/" + item[6]
            self.ui.pic_1.setPixmap(QPixmap(path))
        else:
            self.ui.name_1.setText("无商品")
            self.ui.pic_1.setPixmap(QPixmap(nopic))
        item = gl.get_value("item1")
        if item:
            self.ui.name_2.setText(item[1])
            path = "uis/image/" + item[6]
            self.ui.pic_2.setPixmap(QPixmap(path))
        else:
            self.ui.name_2.setText("无商品")
            self.ui.pic_2.setPixmap(QPixmap(nopic))
        item = gl.get_value("item2")
        if item:
            self.ui.name_3.setText(item[1])
            path = "uis/image/" + item[6]
            self.ui.pic_3.setPixmap(QPixmap(path))
        else:
            self.ui.name_3.setText("无商品")
            self.ui.pic_3.setPixmap(QPixmap(nopic))        
        item = gl.get_value("item3")
        if item:
            self.ui.name_4.setText(item[1])
            path = "uis/image/" + item[6]
            self.ui.pic_4.setPixmap(QPixmap(path))
            
        else:
            self.ui.name_4.setText("无商品")
            self.ui.pic_4.setPixmap(QPixmap(nopic))

    def find_item(self):
        global end
        input = self.ui.Search_input.toPlainText().strip()
        page = gl.get_value("page")
        if(self.tag != -1 and len(input) == 0):
            data = self.query.query_select_tag(self.tag,page)
        elif(self.tag == -1 and len(input) != 0):
            data = self.query.query_search_name(input,page)
        elif(self.tag != -1 and len(input) != 0):
            data = self.query.query_all(page,self.tag, input)
        else:
            data = self.query.query_select_page(page)
        for i in range(4):
            if i < len(data):
                gl.set_value("item%d"%i,data[i])
            else:
                gl.set_value("item%d"%i,None)
        if len(data) < 4:
            end = True
        else:
            end = False

    def nextpage(self):
        if(not end):
            page = gl.get_value("page")
            page = page + 1
            gl.set_value("page",page)
            self.find_item()
            self.show_page()

    def prevpage(self):
        page = gl.get_value("page")
        if page >= 1:
            page = page - 1
            gl.set_value("page",page)
            self.find_item()
            self.show_page()

    def account(self):
        import Accountpage
        self.query.close_connect()
        self.deleteLater()
        self.cams = Accountpage.Accountpage()
        self.cams.show()

    def logsgn(self):
        self.query.close_connect()
        self.deleteLater()
        self.cams = LogSgn.LoginWindow()
        self.cams.show()

    def release(self):
        import Sell_page
        self.query.close_connect()
        self.deleteLater()
        self.cams = Sell_page.Sellpage()
        self.cams.show()
    
    def manage(self):
        import ManageProducts
        self.query.close_connect()
        self.deleteLater()
        self.cams = ManageProducts.ManageProd()
        self.cams.show()
    
    def bought(self):
        import Boughthistory
        self.query.close_connect()
        self.deleteLater()
        self.cams = Boughthistory.Boughtpage()
        self.cams.show()
    
    def sold(self):
        import Soldhistory
        self.query.close_connect()
        self.deleteLater()
        self.cams = Soldhistory.Soldpage()
        self.cams.show()

    def buypage(self,number):
        import Buy_page
        data = gl.get_value("item%s"%number)
        if data:
            gl.set_value("curr_item",number)
            self.query.close_connect()
            self.deleteLater()
            self.cams = Buy_page.Buypage()
            self.cams.show()

    def managerpage(self):
        import Manager
        self.query.close_connect()
        self.deleteLater()
        self.cams = Manager.Managerpage()
        self.cams.show()

    def settag(self,tag):
        if(self.tag == tag):
            self.tag = -1
        else:
            self.tag = tag
        gl.set_value("page",0)
        self.find_item()
        self.show_page()

    def search(self):
        gl.set_value("page",0)
        self.find_item()
        self.show_page()

import sys
if __name__ == '__main__':
    gl._init()
    app = QApplication(sys.argv)
    window = LogSgn.LoginWindow()
    window.show()
    app.exec()