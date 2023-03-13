import sys
import os
import shutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QInputDialog,QFileDialog
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(443, 120)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(50, 40, 301, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Openfile_btn = QtWidgets.QPushButton(self.widget)
        self.Openfile_btn.setObjectName("Openfile_btn")
        self.horizontalLayout.addWidget(self.Openfile_btn)
        self.PathlineEdit = QtWidgets.QLineEdit(self.widget)
        self.PathlineEdit.setObjectName("PathlineEdit")
        self.horizontalLayout.addWidget(self.PathlineEdit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Example"))
        self.Openfile_btn.setText(_translate("Form", "打开文件"))

class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.Openfile_btn.clicked.connect(self.openFile)

    def openFile(self):
        '''get_directory_path = QFileDialog.getExistingDirectory(self,
                                    "选取指定文件夹",
                                    "C:/")
        self.PathlineEdit.setText(str(get_directory_path))'''

        '''get_filenames_path, ok = QFileDialog.getOpenFileNames(self,
                                    "选取多个文件",
                                   "C:/",
                                    "All Files (*);;Text Files (*.txt)")
        if ok:
            self.PathlineEdit.setText(str(' '.join(get_filenames_path)))'''

        get_filename_path, ok = QFileDialog.getOpenFileName(self,
                                    "选取图片",
                                   "C:/",
                                    "Image Files (*.jpg *.png)")
        if ok:
            filename = os.path.basename(str(get_filename_path))
            self.PathlineEdit.setText(str(get_filename_path))
        dirname = os.path.split(os.path.abspath(sys.argv[0]))[0]
        #print(dirname)


        #copy image to /images
        target = 'images'
        target = os.path.join(dirname,target)
        #print(target)
        try:
            shutil.copy(str(get_filename_path), target)
        except IOError as e:
            print("Unable to copy file. %s" % e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())