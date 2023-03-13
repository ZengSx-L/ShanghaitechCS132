from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from pys.Recharge_UI import Ui_widget

class Rechargepage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_widget()
        self.ui.setupUi(self)
        self.ui.Back_btn.clicked.connect(self.back_to_main)
        self.ui.Cancel_btn.clicked.connect(self.back_to_account)
        self.ui.retranslateUi(self)

    def back_to_account(self):
        import Accountpage
        self.deleteLater()
        self.cams = Accountpage.Accountpage()
        self.cams.show()

    def back_to_main(self):
        import Mainpage
        self.deleteLater()
        self.cams = Mainpage.Mainpage()
        self.cams.show()
