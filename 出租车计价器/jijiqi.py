import sys
from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM
import time
from PyQt4 import QtCore, QtGui, uic
qtCreatorFile = "taxi.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

def serverstart():
	s = socket(AF_INET, SOCK_STREAM)
	s.connect(('192.168.4.1', 20000))
	while True:
		msg = s.recv(1)
		if msg == b'a':
			qbj1 = s.recv(4)
			if qbj1 == b'aaaa':
				pass 
			else:
				qbj = str(qbj1,encoding="utf8")
				if qbj[0:3] == '000':
					qbj = '0.' + qbj[3:4]
				elif qbj[0:2] == '00':
					qbj = qbj[2:3] + '.' + qbj[3:4]
				elif qbj[0:1] == '0':
					qbj = qbj[1:3] + '.' +qbj[3:4]
				else :
					qbj = qbj[0:3] + '.' + qbj[3:4]
			global qbj		
		elif msg == b'b':
			dj1 = s.recv(4)
			if dj1 == b'aaaa':
				pass
			else :
				dj = str(dj1,encoding="utf8")
				if dj[0:3] == '000':
					dj = '0.' + dj[3:4]
				elif dj[0:2] == '00':
					dj = dj[2:3] + '.' + dj[3:4]
				elif dj[0:1] == '0':
					dj = dj[1:3] + '.' +dj[3:4]
				else :
					dj = dj[0:3] + '.' + dj[3:4]
			global dj		
		elif msg == b'c':
			dd1 = s.recv(4)
			if dd1 == b'aaaa':
				pass
			else :
				dd = str(dd1,encoding="utf8")
				if dd[0:3] == '000':
					dd = '0.' + dd[3:4]
				elif dd[0:2] == '00':
					dd = dd[2:3] + '.' + dd[3:4]
				elif dd[0:1] == '0':
					dd = dd[1:3] + '.' +dd[3:4]
				else :
					dd = dd[0:3] + '.' + dd[3:4]
			global dd
		elif msg == b'd':
			lc1 = s.recv(4)
			if lc1 == b'aaaa':
				pass
			else :
				lc = str(lc1,encoding="utf8")
				if lc[0:3] == '000':
					lc = '0.' + lc[3:4]
				elif lc[0:2] == '00':
					lc = lc[2:3] + '.' + lc[3:4]
				elif lc[0:1] == '0':
					lc = lc[1:3] + '.' +lc[3:4]
				else :
					lc = lc[0:3] + '.' + lc[3:4]
			global lc
		elif msg == b'e':
			zj1 = s.recv(4)
			if zj1 == b'aaaa':
				pass
			else :
				zj = str(zj1,encoding="utf8")
				if zj[0:3] == '000':
					zj = '0.' + zj[3:4]
				elif zj[0:2] == '00':
					zj = zj[2:3] + '.' + zj[3:4]
				elif zj[0:1] == '0':
					zj = zj[1:3] + '.' +zj[3:4]
				else :
					zj = zj[0:3] + '.' + zj[3:4]
			global zj	

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.fresh_button.clicked.connect(self.taxi_data)	
		
	def taxi_data(self):
		self.qibujia_box.setText('%s' % (qbj))
		self.danjia_box.setText('%s' % (dj))
		self.dengdai_box.setText('%s' % (dd))
		self.lucheng_box.setText('%s' % (lc))
		self.price_box.setText('%s' % (zj))
	
			

if __name__ == "__main__":
    t = Thread(target=serverstart, args=(), daemon=True)
    t.start()
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    exit()