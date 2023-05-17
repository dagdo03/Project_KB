import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(1200, 300, 700, 700)
    win.setWindowTitle("Word Ladder")
    win.setWindowIcon(QIcon("judul.jpeg"))
    win.setToolTip("TurtleCode")
    
    lbl_jawaban = QtWidgets.QLabel(win)
    lbl_jawaban.setText('The answer :')
    lbl_jawaban.move(50, 50)
    
    ans_jawaban = QtWidgets.QLineEdit(win)
    ans_jawaban.move(200, 50)
    
    lbl_hasil = QtWidgets.QLabel(win)
    lbl_hasil.move(200, 200)
    
    def result(self):
        # lbl_hasil = QtWidgets.QLabel(win)
        if ans_jawaban.text() == '5':
            # lbl_hasil = QtWidgets.QLabel(win)
            lbl_hasil.setText('correct')
            # lbl_hasil.move(200, 200)
            # print('correct')
        else:
            # lbl_hasil = QtWidgets.QLabel(win)
            lbl_hasil.setText('wrong')
            # lbl_hasil.move(200, 200)
            # print('wrong')
    
    btn_go = QtWidgets.QPushButton(win)
    btn_go.setText('Go')
    btn_go.clicked.connect(result)
    btn_go.move(200, 130)
    
    win.show()
    sys.exit(app.exec_())
    
window()
