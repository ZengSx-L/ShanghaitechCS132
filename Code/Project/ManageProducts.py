from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from pys.ManageProducts_UI import Ui_ManageProducts_Form
import globalData as gl
from SqlItem import MySQL_Item
class ManageProd(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ManageProducts_Form()
        self.ui.setupUi(self)
        self.ui.Back_btn.clicked.connect(self.back_to_main)
        self.ui.Edit_1_btn.clicked.connect(lambda: self.edit(0))
        self.ui.Edit_2_btn.clicked.connect(lambda: self.edit(1))
        self.ui.Edit_3_btn.clicked.connect(lambda: self.edit(2))
        self.ui.Edit_4_btn.clicked.connect(lambda: self.edit(3))
        self.ui.delete_1_btn.clicked.connect(lambda: self.off(0))
        self.ui.delete_2_btn.clicked.connect(lambda: self.off(1))
        self.ui.delete_3_btn.clicked.connect(lambda: self.off(2))
        self.ui.delete_4_btn.clicked.connect(lambda: self.off(3))
        self.query = MySQL_Item()
        self.ui.Next_page_btn.clicked.connect(self.nextpage)
        self.ui.Prev_page_btn.clicked.connect(self.prevpage)
        self.ui.retranslateUi(self)
        self.find_item()
        self.show_page()
    
    def edit(self,index):
        import Edit
        
        if(gl.get_value("item%d"%index)):
            self.query.close_connect()
            self.deleteLater()
            gl.set_value("curr_item", index)
            self.cams = Edit.Editpage()
            self.cams.show()

    def off(self,index):
        if(gl.get_value("item%d"%index)):
            self.query.delete_item(int(gl.get_value("item%d"%index)[0]))
            self.find_item()
            self.show_page()
        #self.query.close_connect()

    def back_to_main(self):
        import Mainpage
        self.query.close_connect()
        self.deleteLater()
        self.cams = Mainpage.Mainpage()
        self.cams.show()

    def find_item(self):
        global end
        # input = self.ui.Search_input.toPlainText().strip()
        page = gl.get_value("page")
        if(gl.get_value("admin")!=1):
            data = self.query.get_self_item(gl.get_value("user_id"),page)
        else:
            data = self.query.get_all_item(page)
        i = 0
        for i in range(4):
            if i < len(data):
                gl.set_value("item%d"%i,data[i])
            else:
                gl.set_value("item%d"%i,None)
        if len(data) < 4:
            end = True
        else:
            end = False

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