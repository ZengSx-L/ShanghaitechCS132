from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QInputDialog,QFileDialog
from PyQt5.QtCore import Qt
from pys.Sold_UI import Ui_Form
from SqlTrade import MySQL_Trade
from SqlItem import MySQL_Item
import globalData as gl
from time import sleep
end = False
status =  ["已下单","待发货","已发货","完成","已退货","退货完成"]
action = ["发货","收货"]
orders = [0,0,0,0]
page = 0
class Soldpage(QMainWindow):
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

        self.ui.act_btn_1.clicked.connect(lambda:self.act_1(0))
        self.ui.act_btn_2.clicked.connect(lambda:self.act_1(1))
        self.ui.act_btn_3.clicked.connect(lambda:self.act_1(2))
        self.ui.act_btn_4.clicked.connect(lambda:self.act_1(3))

        self.ui.message_btn_1.clicked.connect(lambda:self.chat(0))
        self.ui.message_btn_2.clicked.connect(lambda:self.chat(1))
        self.ui.message_btn_3.clicked.connect(lambda:self.chat(2))
        self.ui.message_btn_4.clicked.connect(lambda:self.chat(3))

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
        data = self.query.query_select_seller(id)
        for i in range(4):
            if (i+page*4) < len(data):
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
            self.ui.price_1.setText(' ')
            self.ui.status_1.setText(' ')
            self.address[0] = None
            self.ui.show_btn1.setEnabled(False)
            self.status[0] = -1
        order = orders[1]
        if order:
            name = self.item_q.get_item(order[1])
            self.ui.name_2.setText(name)
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
            self.ui.price_2.setText(' ')
            self.ui.status_2.setText(' ')
            self.address[1] = None
            self.ui.show_btn2.setEnabled(False)
            self.status[1] = -1
        order = orders[2]
        if order:
            name = self.item_q.get_item(order[1])
            self.ui.name_3.setText(name)
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
            self.ui.price_3.setText(' ')
            self.ui.status_3.setText(' ')
            self.ui.show_btn3.setEnabled(False)
            self.address[2] = None
            self.status[2] = -1      
        order = orders[3]
        if order:
            name = self.item_q.get_item(order[1])
            self.ui.name_4.setText(name)
            self.ui.account_4.setText(str(order[4]))
            self.ui.price_4.setText("%.2f"%order[5])
            self.address[3] = order[6]
            self.ui.show_btn4.setEnabled(True)
            index = order[7]
            self.status[3] = index
            self.ui.status_4.setText(status[index])
        else:
            self.ui.name_4.setText('无')
            self.ui.account_4.setText(' ')
            self.ui.price_4.setText(' ')
            self.ui.status_4.setText(' ')
            self.ui.show_btn4.setEnabled(False)
            self.address[3] = None
            self.status[3] = -1
        self.set_btn_text() 

    def back_to_main(self):
        import Mainpage
        self.query.close_connect()
        self.item_q.close_connect()
        self.deleteLater()
        self.cams = Mainpage.Mainpage()
        self.cams.show()
    
    def show_address(self,id):
        if self.address[id]:
            QMessageBox().information(self, "地址", self.address[id], QMessageBox().Ok)

    def set_btn(self,index,text):
        if text == None:
            act = False
        else:
            act = True
        if act:
            if index == 0:
                self.ui.act_btn_1.setText(text)
                self.ui.act_btn_1.setEnabled(True)
            elif index == 1:
                self.ui.act_btn_2.setText(text)
                self.ui.act_btn_2.setEnabled(True)
            elif index == 2:
                self.ui.act_btn_3.setText(text)
                self.ui.act_btn_3.setEnabled(True)
            elif index == 3:
                self.ui.act_btn_4.setText(text)
                self.ui.act_btn_4.setEnabled(True)
        else:
            if index == 0:
                self.ui.act_btn_1.setEnabled(False)
            elif index == 1:
                self.ui.act_btn_2.setEnabled(False)
            elif index == 2:
                self.ui.act_btn_3.setEnabled(False)
            elif index == 3:
                self.ui.act_btn_4.setEnabled(False)
    
        #print(self.ui.act_btn_3.isEnabled())
    def set_btn_text(self):
        text = []

#status =  ["已下单","待发货","已发货","完成","已退货","退货完成"]
#action = ["发货","收货"]

        for i in self.status:
            if i == 1:
                text.append(action[0])
            elif i == 4 :
                text.append(action[1])

            else:
                text.append(None)

            #print(i)
        
        for i in range(4):
            self.set_btn(i,text[i])

    def act_1(self,index):
        #usr = gl.get_value("user_id")
        s = self.status[index]
        if s == 1:
          trade = orders[index][0]
          self.query.set_status(trade,2)
          #self.status[index] = 2
          #self.set_btn_text()
          self.deliver(index)
        elif s == 4:
                buyer = orders[index][3]
                me = gl.get_value("user_id")
                trade = orders[index][0]
                price =  float(orders[index][5])
                b = float(self.query.get_balance(buyer))
                myb = float(self.query.get_balance(me))
                if myb <= price:
                    QMessageBox().information(self, "注意", "余额不足，无法退款，请前往用户界面充值",
                                                 QMessageBox().Ok)
                    return
                else:
                    self.query.set_balance(me,myb-price)
                if (b + price > 999999.99):
                    b = 999999.99
                else:
                    b = b + price
                self.query.set_status(trade,5)
                self.query.set_balance(buyer,b)
                QMessageBox().information(self, "Success!", "退货完成\n买家已收款", QMessageBox().Ok)
        self.find_order()
        self.show_orders()
    
    def deliver(self,index):
        sleep(2)
        if index == 0:
            self.ui.status_1.setText("发货中")
            self.ui.status_1.repaint()
        elif index == 1:
            self.ui.status_2.setText("发货中")
            self.ui.status_1.repaint()
        elif index == 2:
            self.ui.status_3.setText("发货中")
            self.ui.status_1.repaint()
        elif index == 3:
            self.ui.status_4.setText("发货中")
            self.ui.status_1.repaint()
                
        sleep(2)
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
        
    def chat(self, index):
        import Chatlog
        if orders[index] == None:
            return
        other = orders[index][3]
        gl.set_value("other",other)
        dia = Chatlog.Chatpage()
        dia.exec_()   
import sys
if __name__ == '__main__':
    gl._init()
    #for debug
    gl.set_value("user_id",233)
    app = QApplication(sys.argv)
    window = Soldpage()
    window.show()
    app.exec()
