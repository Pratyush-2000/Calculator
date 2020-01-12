import sys
import array
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(200, 200))    
        self.setWindowTitle("PyQt button example - pythonprogramminglanguage.com") 
        
        rows, cols = (3, 3) 
        button = [[0]*cols]*rows 
        for i in range(3):
         for j in range(3):
        		print(i,j)
        		button[i][j] = QPushButton(str(i*3+j+1), self)
        		button[i][j].clicked.connect(self.clickMethod)
        		button[i][j].resize(50,50)
        		button[i][j].move(0+50*j,150-50*i)   
        

           


    def clickMethod(self):
        print('Clicked Pyqt button.')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
