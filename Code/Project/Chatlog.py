
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt, QRect
from pys.Chatlog_UI import Ui_Dialog
from SqlMessage import MySQL_Message
import globalData as gl
end = False
msg = [None,None,None,None,None] 
class Chatpage(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.query = MySQL_Message()

        self.this = gl.get_value("user_id")
        self.other = gl.get_value("other")

        self.ui.back.clicked.connect(self.back)
        self.ui.send.clicked.connect(self.send)

        self.ui.prev.clicked.connect(self.prevpage)
        self.ui.next.clicked.connect(self.nextpage)

        self.data = self.query.query_select(self.this,self.other)
        
        self.ui.talk_partner.setText(self.query.get_name(self.other))
        self.total = len(self.data)
        if self.total >= 5:
            self.page = self.total // 5
        else:
            self.page = 0
        self.find_message()
        self.show_message()
    def back(self):
        self.query.close_connect()
        self.accept()
    def send(self):
        Text = self.ui.typein.toPlainText()
        
        if len(Text) == 0:
            QMessageBox().information(self, "注意", "内容不能为空", QMessageBox().Ok)
            return
        if len(Text) > 99:
            QMessageBox().information(self, "注意", "内容字数超上限（100字）", QMessageBox().Ok)
            return
        self.ui.typein.setText('')
        data = [self.this,self.other,Text]
        self.query.query_insert(data)
        self.find_message()
        self.total = len(self.data)
        if self.total >= 5:
            self.page = self.total // 5
        else:
            self.page = 0
        self.show_message()

    def find_message(self):
        global end
        self.data = self.query.query_select(self.this,self.other)

        for i in range(5):
            if (i+self.page*5) < len(self.data):
                msg[i] = self.data[i+self.page*5]
            else:
                msg[i] = None
        if msg[4] == None:
            end = True
        else:
            end = False
    def show_message(self):
        m = msg[0]
        if m:
            name = self.query.get_name(m[0])
            name = name + ":"
            self.ui.text1.setText(name+m[2])
        else:
            self.ui.text1.setText(" ")
        m = msg[1]
        if m:
            name = self.query.get_name(m[0])
            name = name + ":"
            self.ui.text2.setText(name+m[2])
        else:
            self.ui.text2.setText(" ")
        m = msg[2]
        if m:
            name = self.query.get_name(m[0])
            name = name + ":"
            self.ui.text3.setText(name+m[2])
        else:
            self.ui.text3.setText(" ")
        m = msg[3]
        if m:
            name = self.query.get_name(m[0])
            name = name + ":"
            self.ui.text4.setText(name+m[2])
        else:
            self.ui.text4.setText(" ")
        m = msg[4]
        if m:
            name = self.query.get_name(m[0])
            name = name + ":"
            self.ui.text5.setText(name+m[2])
        else:
            self.ui.text5.setText(" ")

    def nextpage(self):
        if(not end):
            self.page = self.page + 1
            self.find_message()
            self.show_message()
    def prevpage(self):
        if self.page >= 1:
            self.page = self.page - 1
            self.find_message()
            self.show_message()
