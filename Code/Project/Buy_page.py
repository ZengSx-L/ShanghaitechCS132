from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt, QRect
from pys.Buy_UI import Ui_Buy_Form
from SqlItem import MySQL_Item
from SqlTrade import MySQL_Trade
import globalData as gl 
class Buypage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Buy_Form()
        self.ui.setupUi(self)

        self.query = MySQL_Item()
        self.users = MySQL_Trade()
        self.ui.Back_btn.clicked.connect(self.back_to_main)

        self.ui.prev_page_btn.clicked.connect(self.prevpage)
        self.ui.next_page_btn.clicked.connect(self.nextpage)

        self.ui.retranslateUi(self)
        curr = gl.get_value("curr_item")
        data = gl.get_value("item%d"%curr)
        self.item = data[0]
        self.ui.name_label.setText(data[1])
        self.price = data[2]
        self.price = float(self.price)
        self.ui.price_label.setText("%.2f"%self.price)
        self.seller = data[3]
        self.ui.stock_label.setText("%d"%data[4])
        self.ui.Discription.setText(data[5])
        self.ui.Pic.setPixmap(QPixmap("uis/image/"+data[6]))

        self.comment = self.query.query_select_comment(self.item)
        self.total_comment = len(self.comment)
        self.comment_index = 0
        self.show_comment()


        if(gl.get_value("admin")!=1 and self.seller != gl.get_value("user_id")):
            self.ui.Buy_btn = QPushButton(self)
            self.ui.Buy_btn.setGeometry(QRect(660, 470, 201, 71))
            self.ui.Buy_btn.setText("购买")
            self.ui.Buy_btn.clicked.connect(self.buyproduct)
    
    def back_to_main(self):
        import Mainpage
        self.query.close_connect()
        self.users.close_connect()
        self.deleteLater()
        self.cams = Mainpage.Mainpage()
        self.cams.show()

    def buyproduct(self):
        import Confirm
        dia = Confirm.ConfirmDia()
        dia.exec_()

    def chat(self):
        import Chatlog
        gl.set_value("other",self.seller)
        dia = Chatlog.Chatpage()
        dia.exec_()        

    def nextpage(self):
        if(self.total_comment > self.comment_index + 1):
            self.comment_index = self.comment_index + 1
            self.show_comment()
    def prevpage(self):
        if self.comment_index >= 1:
            self.comment_index = self.comment_index - 1
            self.show_comment()
    def show_comment(self):
        if self.total_comment > self.comment_index:
            usr = self.users.get_name(self.comment[self.comment_index][1])
            usr = usr + ":\n"
            self.ui.Comment.setText(usr+self.comment[self.comment_index][2])
        else:
            self.ui.Comment.setText("暂无评论")

