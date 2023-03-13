from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from pys.Comment_UI import Ui_Dialog

class Commentpage(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # self.ui.Back_btn.clicked.connect(self.back_to_main)
        # self.ui.Comment_btn.clicked.connect(self.comment)
        self.ui.retranslateUi(self)