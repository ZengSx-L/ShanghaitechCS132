from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QInputDialog,QFileDialog
from PyQt5.QtCore import Qt
from pys.Manager_UI import Ui_Form
from SqlTrade import MySQL_Trade
from SqlItem import MySQL_Item
import globalData as gl
end = False
status =  ["已下单","已付款","已发货","完成","已退货","退货完成"]
action = ["付款","收货","评价"]
action_2 = ["取消","退货"] 
orders = [0,0,0,0]
page = 0
class Managerpage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.status = [-1,-1,-1,-1]
        self.address = [None,None,None,None]
        
        self.ui.Back_btn.clicked.connect(self.back_to_main)
        self.ui.Prev_page_btn.clicked.connect(self.prevpage)
        self.ui.Next_page_btn.clicked.connect(self.nextpage)

        self.ui.show_btn1.clicked.connect(lambda:self.show_address(0))
        self.ui.show_btn2.clicked.connect(lambda:self.show_address(1))
        self.ui.show_btn3.clicked.connect(lambda:self.show_address(2))
        self.ui.show_btn4.clicked.connect(lambda:self.show_address(3))
        
        self.ui.retranslateUi(self)
        self.query = MySQL_Trade()
        self.item_q = MySQL_Item()
        self.find_order()
        self.show_orders()
        #self.set_btn_text()
    def find_order(self):
        global end
        global orders
        id = gl.get_value("user_id")
        data = self.query.query_select_all()
        for i in range(4):
            if (i + page *4) < len(data):
                orders[i] = data[i+page*4]
            else:
                orders[i] = None
        if orders[3] == None:
            end = True
        else:
            end = False
    def show_orders(self):
#id  item_id seller_id buyer_id amount price address status
        order = orders[0]

        if order:
            name = self.item_q.get_item(order[1])
            self.ui.name_1.setText(name)
            self.ui.seller_1.setText(self.query.get_name(order[2]))
            self.ui.buyer_1.setText(self.query.get_name(order[3]))
            self.ui.account_1.setText(str(order[4]))
            self.ui.price_1.setText("%.2f"%order[5])
            self.address[0] = order[6]
            self.ui.show_btn1.setEnabled(True)
            index = order[7]
            self.status[0] = index
            self.ui.status_1.setText(status[index])
        else:
            self.ui.name_1.setText('无')
            self.ui.account_1.setText(' ')
            self.ui.buyer_1.setText(' ')
            self.ui.seller_1.setText(' ')
            self.ui.price_1.setText(' ')
            self.ui.status_1.setText(' ')
            self.address[0] = None
            self.ui.show_btn1.setEnabled(False)
            self.status[0] = -1
        order = orders[1]
        if order:
            name = self.item_q.get_item(order[1])
            self.ui.name_2.setText(name)
            self.ui.seller_2.setText(self.query.get_name(order[2]))
            self.ui.buyer_2.setText(self.query.get_name(order[3]))
            self.ui.account_2.setText(str(order[4]))
            self.ui.price_2.setText("%.2f"%order[5])
            self.address[1] = order[6]
            self.ui.show_btn2.setEnabled(True)
            index = order[7]
            self.status[1] = index
            self.ui.status_2.setText(status[index])
        else:
            self.ui.name_2.setText('无')
            self.ui.account_2.setText(' ')
            self.ui.buyer_2.setText(' ')
            self.ui.seller_2.setText(' ')
            self.ui.price_2.setText(' ')
            self.ui.status_2.setText(' ')
            self.address[1] = None
            self.ui.show_btn2.setEnabled(False)
            self.status[1] = -1
        order = orders[2]
        if order:
            name = self.item_q.get_item(order[1])
            self.ui.name_3.setText(name)
            self.ui.seller_3.setText(self.query.get_name(order[2]))
            self.ui.buyer_3.setText(self.query.get_name(order[3]))
            self.ui.account_3.setText(str(order[4]))
            self.ui.price_3.setText("%.2f"%order[5])
            self.address[2] = order[6]
            self.ui.show_btn3.setEnabled(True)
            index = order[7]
            self.status[2] = index
            self.ui.status_3.setText(status[index])
        else:
            self.ui.name_3.setText('无')
            self.ui.account_3.setText(' ')
            self.ui.buyer_3.setText(' ')
            self.ui.seller_3.setText(' ')
            self.ui.price_3.setText(' ')
            self.ui.status_3.setText(' ')
            self.ui.show_btn3.setEnabled(False)
            self.address[2] = None
            self.status[2] = -1      
        order = orders[3]
        if order:
            name = self.item_q.get_item(order[1])
            self.ui.name_4.setText(name)
            self.ui.seller_4.setText(self.query.get_name(order[2]))
            self.ui.buyer_4.setText(self.query.get_name(order[3]))
            self.ui.account_4.setText(str(order[4]))
            self.ui.price_4.setText("%.2f"%order[5])
            self.address[3] = order[6]
            self.ui.show_btn4.setEnabled(True)
            index = order[7]
            self.status[3] = index
            self.ui.status_4.setText(status[index])
        else:
            self.ui.name_4.setText('无')
            self.ui.buyer_4.setText(' ')
            self.ui.seller_4.setText(' ')
            self.ui.account_4.setText(' ')
            self.ui.price_4.setText(' ')
            self.ui.status_4.setText(' ')
            self.ui.show_btn4.setEnabled(False)
            self.address[3] = None
            self.status[3] = -1
    def back_to_main(self):
        import Mainpage
        self.deleteLater()
        self.cams = Mainpage.Mainpage()
        self.cams.show()
    def nextpage(self):
        global page
        if(not end):
            page = page + 1
            gl.set_value("page",page)
            self.find_order()
            self.show_orders()

    def prevpage(self):
        global page
        if page >= 1:
            page = page - 1
            gl.set_value("page",page)
            self.find_order()
            self.show_orders()

    def show_address(self,id):
        if self.address[id]:
            QMessageBox().information(self, "地址", self.address[id], QMessageBox().Ok)