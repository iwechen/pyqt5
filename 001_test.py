import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication ,QMessageBox

from PyQt5.QtGui import QIcon,QFont

from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建鼠标定位说明
        # 调整字体大小
        QToolTip.setFont(QFont('sanSerif',10))
        self.setToolTip('空格说明')
        btn = QPushButton('button',self)
        btn.setToolTip('1.这是按钮说明\n2.鼠标停几秒就显示')
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        # 创建关闭按钮
        abtn = QPushButton('关闭',self)
        abtn.clicked.connect(QCoreApplication.instance().quit)
        abtn.resize(abtn.sizeHint())
        abtn.move(100,100)

        # 设置窗口大小
        self.setGeometry(300,300,300,220)
        # self.setWindowIcon(QIcon('web.png'))
        self.setWindowTitle('Message')
        self.show()

    def closeEvent(self,event):
        reply = QMessageBox.question(self,'Message',"Are you sure to quit?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())










