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

    
    
    menu = QtGui.QMenuBar(self)
    exit = menu.addMenu('&File')
    exit.addAction(exitAction)
    info = menu.addMenu('&Info')
    info.addAction(infoAction)
    
    button= QtGui.QPushButton("Download Menu", self)
    button.move(70, 80)
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
    mesi = {1:"gennaio", 2:"febbraio", 3:"marzo", 4:"aprile",5:"maggio", 6:"giugno", 7:"luglio", 
	    8:"agosto", 9:"settembre", 10:"ottobre", 11:"novembre", 12:"dicembre"}
    return mesi.get(i)
   
  def onActive(self):
    d = date.today().day
    m = date.today().month
    M = self.mese(m)
    try:
      webbrowser.open("http://www.adisu.sa.it/fileadmin/user_upload/menu/menu_del_giorno_%d_"% d + M +"__2013_img.pdf")
    except webbrowser.Error:
      print(webbrowser.Error)
    
def main():
  app = QtGui.QApplication(sys.argv)
  ex = Example()
  sys.exit(app.exec_())
  
if __name__== '__main__':
  main()
