# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PyQt5.QtWidgets import *
from calculate import Ui_MainWindow
from Calculate_a import calculate_a
from Calculate_Pb import calculate_Pb
from Calculate_s import calculate_s
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # 继承(QMainWindow,Ui_MainWindow)父类的属性
        super(MainWindow, self).__init__()
        # 初始化界面组件
        self.setupUi(self)
        self.i = 0
        self.pushButton.clicked.connect(self.Algorithm_1)
        self.pushButton_2.clicked.connect(self.Algorithm_2)
        self.pushButton_3.clicked.connect(self.Algorithm_3)
        self.pushButton_4.clicked.connect(self.clear_1)
        self.pushButton_5.clicked.connect(self.clear_2)
        self.pushButton_6.clicked.connect(self.clear_3)

    def Algorithm_1(self):
        self.a1 = int(self.lineEdit.text())
        self.s1 = int(self.lineEdit_2.text())
        self.Pb1 = calculate_Pb(self.a1, self.s1)
        self.textBrowser.setText(str(self.Pb1))

    def Algorithm_2(self):
        self.s2 = int(self.lineEdit_3.text())
        self.Pb2 = float(self.lineEdit_4.text())
        self.a2 = calculate_a(self.s2, self.Pb2)
        self.textBrowser_2.setText(str(self.a2))

    def Algorithm_3(self):
        self.a3 = int(self.lineEdit_5.text())
        self.Pb3 = float(self.lineEdit_6.text())
        self.s3 = calculate_s(self.a3, self.Pb3)
        self.textBrowser_3.setText(str(self.s3))

    def clear_1(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.textBrowser.clear()

    def clear_2(self):
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.textBrowser_2.clear()

    def clear_3(self):
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.textBrowser_3.clear()

if __name__ == '__main__':

    # 创建QApplication 固定写法
    app = QApplication(sys.argv)
    # 实例化界面
    window = MainWindow()
    # 显示界面
    window.show()
    # 阻塞，固定写法
    sys.exit(app.exec_())
