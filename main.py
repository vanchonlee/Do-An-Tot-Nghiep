import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi

class Li(QDialog):
    def __init__(self):
        super(Li,self).__init__()
        loadUi('main.ui',self)
        self.setWindowTitle('chon')

app = QApplication(sys.argv)
widget = Li()
widget.show()
sys.exit(app.exec_())
