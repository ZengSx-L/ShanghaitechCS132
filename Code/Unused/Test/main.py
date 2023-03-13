import sys

from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtCore import QEvent
from SqlLogin import MySQL_login
from pys.Mainpage_UI import Ui_Form
from pys.ManageProducts_UI import Ui_ManageProducts_Form
from pys.Edit_UI import Ui_Edit_Form
from pys.Login_UI import Ui_LogInSignUpForm
from pys.Signup_UI import Ui_RegisterForm
import globalData as gl 

class Mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #self.ui.Edit_1_btn.clicked.connect(self.editForm)
        self.show()
'''
    def editForm(self):
        self.deleteLater()
        self.cams = EditWindow()
        self.cams.show()

class EditWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Edit_Form()
        self.ui.setupUi(self)
        self.show()
'''
class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_LogInSignUpForm()
        self.ui.setupUi(self)
        self.ui.Sgn_btn.clicked.connect(self.reg_form)
        self.ui.Log_btn.clicked.connect(self.login_form)
        self.query = MySQL_login()
        self.show()
        self.init_ui()

    def login_form(self):
        telephone = self.ui.Log_input.text()
        password = self.ui.Password_input.text()

        if self.query.query_select_login_passwd(telephone, password):
            user = self.query.query_select_current_user(telephone)
            data = []
            for index in range(len(user[0])):
                data.append(user[0][index])
            gl.set_value("user_id",data[0])
            gl.set_value("name",data[1])
            gl.set_value("user_name",data[2])
            gl.set_value("admin",data[3])
            self.run_main_window()
        else:
            QtWidgets.QMessageBox().critical(self, "Error", "账号或密码错误", QtWidgets.QMessageBox().Ok)

    def init_ui(self):
        pass

    def reg_form(self):
        self.deleteLater()
        self.cams = SignupWindow()
        self.cams.show()

    def run_main_window(self):
        self.deleteLater()
        self.cams = Mainwindow()
        self.cams.show()
class SignupWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(SignupWindow, self).__init__()
        self.ui = Ui_RegisterForm()
        self.ui.setupUi(self)
        self.ui.reg_btn.clicked.connect(self.btn_register)
        self.ui.back_btn.clicked.connect(self._btn_back)
        self.query = MySQL_login()
        self.cntr = 0
        self.ui.password_input.installEventFilter(self)
        self.ui.password_rpt_input.installEventFilter(self)
        self.show()
        self.init_ui()

    def init_ui(self):
        pass

    def btn_register(self):
        name = self.ui.name_input.text()
        uname = self.ui.uname_input.text()
        email = self.ui.email_input.text()
        telephone = self.ui.phone_input.text()
        password = self.ui.password_input.text()
        password_rpt = self.ui.password_rpt_input.text()
        data = [name,uname, email, telephone, password]

        if all(data):
            if self.query.query_check_user(telephone):
                if password == password_rpt:
                    self.query.query_insert(data)
                    print(self.query.query_select_all())
                    self.run_login_window()
                else:
                    QtWidgets.QMessageBox().critical(self, "Error", "输入密码不相同",
                                                     QtWidgets.QMessageBox().Ok)
            else:
                QtWidgets.QMessageBox().critical(self, "Error", "该手机号已注册",
                                                 QtWidgets.QMessageBox().Ok)
        else:
            QtWidgets.QMessageBox().critical(self, "Error", "填写不完整", QtWidgets.QMessageBox().Ok)

    def _btn_back(self):
        self.run_login_window()

    def run_login_window(self):
        self.deleteLater()
        self.cams = LoginWindow()
        self.cams.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = LoginWindow()
    application.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    gl._init()
    main()