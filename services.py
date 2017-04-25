from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
import sys



class APIServer(QThread):
	def __init__ (self):
		QThread.__init__(self)
		

	def run(self):
		try:
			from ServerBroker import inicializador
		except Exception as e:
			raise e
		inicializador.ini()
		