import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from test import *
from form import Ui_Form
import apprcc_rc

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.child = ChildForm()
        self.myadd.triggered.connect(self.childshow)

    def childshow(self):
        self.gridLayout_2.addWidget(self.child)# 这里生成窗体有问题
        self.child.show()
        self.gridLayout_2.addWidget(self.label_3)
class ChildForm(QWidget, Ui_Form):
    def __init__(self):
        super(ChildForm, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec())