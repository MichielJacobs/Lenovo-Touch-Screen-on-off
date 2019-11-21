import sys
import datetime
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):

	def __init__(self, icon, parent=None):
		QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)		
		menu = QtWidgets.QMenu(parent)
		onAction = menu.addAction("Touch Screen ON")
		offAction = menu.addAction("Touch Screen OFF")
		aboutAction = menu.addAction("About")
		menu.addSeparator()
		exitAction = menu.addAction("Exit")
				
		menu.triggered.connect(self.processtrigger)
		self.setContextMenu(menu)


	def processtrigger(self,q):		
		if q.text () == "Exit":
			sys.exit()

		if q.text() == "About":
			msg = QMessageBox()
			msg.setTextFormat(Qt.RichText)
			msg.setText("This app is created by Michiel Jacobs <br> Visit <a href='https://github.com/MichielJacobs/TouchScreenToggle'>my github page</a> for more information. <br/><div>Icons made by <a href='https://www.flaticon.com/authors/pixel-perfect' title='Pixel perfect'>Pixel perfect</a> from <a href='https://www.flaticon.com/' title='Flaticon'>www.flaticon.com</a></div>")
			msg.setWindowTitle("About TouchScreenToggle")
			msg.exec_()

		if q.text() == "Touch Screen ON":
			self.turnTouchOn()
		
		if q.text() == "Touch Screen OFF":
			self.turnTouchOff()

	def turnTouchOn(self):
		os.system('start devmanview-x64/DevManView.exe /enable "HID-compliant touch screen"')
		self.setIcon(QtGui.QIcon("img/on.svg"))

	def turnTouchOff(self):
		os.system('start devmanview-x64/DevManView.exe /disable "HID-compliant touch screen"')
		self.setIcon(QtGui.QIcon("img/off.svg"))



def main(image):
	app = QtWidgets.QApplication(sys.argv)
	app.setQuitOnLastWindowClosed(False) #needed because there is no window by default. Otherwise closing a QMessageBox will result in quiting the app
	w= QtWidgets.QWidget()		
	trayIcon = SystemTrayIcon(QtGui.QIcon(image), w)
	trayIcon.show()
	sys.exit(app.exec_())	



if __name__ == '__main__':
	on="img/on.svg"
	main(on)
