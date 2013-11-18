import sys
from PyQt4 import QtGui
import webbrowser
from datetime import *

class Example(QtGui.QMainWindow):
  
  def __init__(self):
    super(Example, self).__init__()
    self.initUI()
    
  def initUI(self):
    
    exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
    exitAction.setShortcut('Ctrl+Q')
    exitAction.setStatusTip('Exit application')
    exitAction.triggered.connect(QtGui.qApp.quit)
    infoAction = QtGui.QAction('&Info', self)
    infoAction.setShortcut('Ctrl+I')
    infoAction.setStatusTip('Info application')
    infoAction.triggered.connect(self.infoout)
    
    label = QtGui.QLabel("Downloader Menu Mensa", self)
    label.move(50,30)
    label.resize(label.sizeHint())
    
    menu = QtGui.QMenuBar(self)
    exit = menu.addMenu('&File')
    exit.addAction(exitAction)
    info = menu.addMenu('&Info')
    info.addAction(infoAction)
    
    button= QtGui.QPushButton("Download Menu", self)
    button.move(50, 80)
    button.clicked.connect(self.onActive)
    
    
    self.setGeometry(300,300,250,200)
    self.setWindowTitle("Downloader Menu Mensa")
    self.show()
    
  def infoout(self):   
    window = QtGui.QMessageBox(self)
    window.setText('< Developed by Marco Schettini >  ')
    window.icon()
    window.exec_()
    
    
  def mese(self, i):
    if i == 1:
      i = "gennaio"
    elif i == 2:
      i = "febraio"
    elif i == 3:
      i = "marzo"
    elif i == 4:
      i = "aprile"
    elif i == 5:
      i = "maggio"
    elif i == 6:
      i = "giugno"
    elif i == 7:
      i = "luglio"
    elif i == 8:
      i = "agosto"
    elif i == 9:
      i = "settembre"
    elif i == 10:
      i = "ottobre"
    elif i == 11:
      i = "novembre"
    elif i == 12:
      i = "dicembre"
    return i 
   
  def onActive(self):
    d = date.today().day
    m = date.today().month
    M = self.mese(m)
    webbrowser.open("http://www.adisu.sa.it/fileadmin/user_upload/menu/menu_del_giorno_%d_"% d + M +"__2013_img.pdf")
    
def main():
  app = QtGui.QApplication(sys.argv)
  ex = Example()
  sys.exit(app.exec_())
  
if __name__== '__main__':
  main()
