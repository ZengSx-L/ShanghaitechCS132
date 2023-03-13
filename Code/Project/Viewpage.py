from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
import pys.View_UI

class Viewpage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = pys.View_UI.Ui_View_Form()
        self.ui.setupUi(self)
        self.ui.Back_btn.clicked.connect(self.back_to_main)
        self.ui.back_to_bought_btn.clicked.connect(self.back_to_bought)
        self.ui.retranslateUi(self)
    
    def back_to_bought(self):
        import Boughthistory
        self.deleteLater()
        self.cams = Boughthistory.Boughtpage()
        self.cams.show()

    def back_to_main(self):
        import Mainpage
        self.deleteLater()
        self.cams = Mainpage.Mainpage()
        self.cams.show()