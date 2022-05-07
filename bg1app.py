from PyQt5 import QtWidgets
from bg1 import Ui_Form
import sys
import sqlite3
from addapp import myadd
from anaapp import myana
from displayapp import mydisplay
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets

class myapp(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(myapp,self).__init__()
        self.setupUi(self)
        #self.pushButton.clicked.connect(self.openwindowadd)
        self.pushButton_4.clicked.connect(self.openwindowana)
        self.pushButton_2.clicked.connect(self.openwindowdisplay)
    
    def openwindowana(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=myana()
        self.ui.setupUi(self.window)
        self.window.show()
    def openwindowdisplay(self):
        print("hiii")
        self.window=QtWidgets.QMainWindow()
        ui=mydisplay()
        ui.setupUi(self.window)
        self.window.show()
    
 
if __name__=="__main__":
    app =QtWidgets.QApplication(sys.argv)
    Form = myapp()
    Form.show()
    sys.exit(app.exec_())
    