from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
import sys
from inicializador import start, stop


class APIServer(QThread):
	def __init__ (self, parent=None):
		QThread.__init__(self)		

	def run(self):	
		start()

	def stopserver(self):
		stop()
		print("Parando servidor")