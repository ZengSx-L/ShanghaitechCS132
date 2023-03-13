import sys
import os
import shutil
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QInputDialog,QFileDialog
from pys.Edit_UI import Ui_Sell_Form
from SqlItem import MySQL_Item
import globalData as gl 
import time

dirname = os.path.split(os.path.abspath(sys.argv[0]))[0]
target = os.path.join(dirname,'uis/image')
file_path = ' '
filename = None
change  = False
class Editpage(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.taglist = ["饮食","衣饰","日用"]
        self.ui = Ui_Sell_Form()
        self.ui.setupUi(self)
        self.ui.Release_btn.clicked.connect(self.release)
        self.ui.Back_btn.clicked.connect(self.back_to_main)
        self.ui.Openfile_btn.clicked.connect(self.openFile)
        self.ui.Tag_select.addItem(self.taglist[0])
        self.ui.Tag_select.addItem(self.taglist[1])
        self.ui.Tag_select.addItem(self.taglist[2])
        self.ui.Tag_select.setCurrentIndex(0)
        self.curr = gl.get_value("curr_item")
        data = gl.get_value("item%d"%self.curr)
        self.id = data[0]
        print(data)
        global filename
        global file_path
        self.ui.name_input.setText(data[1])
        price = float(data[2])
        self.ui.price_input.setText("%.2f"%price)
        self.ui.stock_input.setText("%d"%data[4])
        self.ui.info_input.setPlainText(data[5])
        filename = data[6]
        file_path = os.path.join(target,filename)
        self.ui.Picture.setPixmap(QtGui.QPixmap(file_path))

        price_reg = QtCore.QRegExp('^([0]|[1-9][0-9]{0,5})(?:\\.\\d{1,2})?$|(^\\t?$)')
        validator = QtGui.QRegExpValidator(self)
        validator.setRegExp(price_reg)
        self.ui.price_input.setValidator(validator)

        stock_reg = QtCore.QRegExp('[1-9][0-9]{0,5}')
        validator_2 = QtGui.QRegExpValidator(self)
        validator_2.setRegExp(stock_reg)
        self.ui.stock_input.setValidator(validator_2)
        self.ui.retranslateUi(self)

        self.query = MySQL_Item()
    
    def back_to_main(self):
        import Mainpage
        self.query.close_connect()
        self.deleteLater()
        self.cams = Mainpage.Mainpage()
        self.cams.show()
    def openFile(self):
        global file_path
        global filename
        file_path, ok = QFileDialog.getOpenFileName(self,
                                    "选取图片",
                                   dirname,
                                    "Image Files (*.jpg *.png)")
        if ok:
            global change
            filename = os.path.basename(str(file_path))
            self.ui.PathlineEdit.setText(str(file_path))
            self.ui.Picture.setPixmap(QtGui.QPixmap(file_path))
            change = True
        else:
            filename = None
    def copyFile(self):
            global filename
            newpath = os.path.join(target,filename)
            t = filename.split('.')[-1]
            if os.path.exists(newpath):
                return False
            try:
                shutil.copy(str(file_path), target)
                newname=str(int(time.time()))+'.'+t
                filename = newname
                rename = os.path.join(target,newname)
                os.rename(newpath,rename)
                return True
            except IOError as e:
                print("Unable to copy file. %s" % e)
                return False


    def release(self):
        itemname = self.ui.name_input.text().strip()
        price = self.ui.price_input.text()
        amount = self.ui.stock_input.text()
        intro = self.ui.info_input.toPlainText()
        #valid check
        if(len(itemname)==0):
            QMessageBox().warning(self, "Error", "请输入商品名称",QMessageBox().Ok)
            return
        if(price):
            try:
                price = float(price)
            except:
                QMessageBox().warning(self, "Error", "价格须为非负数",QMessageBox().Ok)
                return
        else:
            QMessageBox().warning(self, "Error", "请输入价格",
                                                QMessageBox().Ok)
            return
        
        if(amount):
            try:
               amount =  int(amount)
            except:
                QMessageBox().warning(self, "Error", "数量须为数字",QMessageBox().Ok)
                return
            if(int(amount) < 0):
                QMessageBox().warning(self, "Error", "数量须为非负数",QMessageBox().Ok)
                return
        else:
            QMessageBox().warning(self, "Error", "请输入商品数量",
                                                QMessageBox().Ok)
            return
        if(not filename):
            QMessageBox().warning(self, "Error", "请选择商品图片",
                                                QMessageBox().Ok)
            return
        tagIndex = self.ui.Tag_select.currentIndex()



        #item_name,seller_id,price,stock,intro, img_name,tag
        if len(itemname) > 19:
            QMessageBox().warning(self, "Error", "商品名字数超上限（20字）",QMessageBox().Ok)
            return
        if len(intro) > 99:
            QMessageBox().warning(self, "Error", "商品介绍数超上限（100字）",QMessageBox().Ok)
            return


        if change:
            if(not self.copyFile()):
                QMessageBox().warning(self, "Error", "上传图片时出现错误",QMessageBox().Ok)
                return
        data = [itemname,gl.get_value("user_id"),price,amount,intro,filename,tagIndex]
        self.query.update_item(data,self.id)
        QMessageBox().information(self, "Success!", "商品修改成功!", QMessageBox().Ok)
        self.back_to_main()
        #print(self.query.query_select_all())
'''def main():
    app = QApplication(sys.argv)
    application = Editpage()
    application.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    gl._init()
    gl.set_value("user_id",233)
    main()
'''