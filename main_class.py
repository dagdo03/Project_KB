import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class my_window(QMainWindow):
    def __init__(self):
        super(my_window, self).__init__()
        self.setGeometry(1200, 300, 700, 700)
        self.setWindowTitle("Word Ladder")
        self.setToolTip("WordLadder")
        self.setWindowIcon(QIcon("judul.jpeg"))
        self.initUI()
        
    def initUI(self):
        self.lbl_ans = QtWidgets.QLabel(self)
        self.lbl_ans.setText("The answer :")
        self.lbl_ans.move(50, 50)
        
        self.txt_input = QtWidgets.QLineEdit(self)
        self.txt_input.move(200, 50)
        self.txt_input.resize(200, 32)
        
        self.lbl_hasil = QtWidgets.QLabel(self)
        self.lbl_hasil.move(200, 200)
    
        self.btn_go = QtWidgets.QPushButton(self)
        self.btn_go.setText('Go')
        self.btn_go.clicked.connect(self.result)
        self.btn_go.move(200, 130)
        
    def result(self):
        # lbl_hasil = QtWidgets.QLabel(win)
        if self.txt_input.text() == '2':
            # lbl_hasil = QtWidgets.QLabel(win)
            self.lbl_hasil.setText('correct')
            # lbl_hasil.move(200, 200)
            # print('correct')
        else:
            # lbl_hasil = QtWidgets.QLabel(win)
            self.lbl_hasil.setText('wrong')
            # lbl_hasil.move(200, 200)
            # print('wrong')
    
def window():
    app = QApplication(sys.argv)
    win = my_window()
    win.show()
    sys.exit(app.exec_())
    
window()