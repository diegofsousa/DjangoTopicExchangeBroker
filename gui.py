from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys, os, subprocess

from services import APIServer


class index(QDialog):
	def __init__(self, parent=None):
		super(index, self).__init__(parent)

		self.labelAPI = QLabel("API Rest (Rest atualmente inativo)")
		self.buttonStartAPI = QPushButton("Start Rest")
		vboxAPI = QVBoxLayout()
		vboxAPI.addWidget(self.labelAPI)
		vboxAPI.addWidget(self.buttonStartAPI)

		self.labelBroker = QLabel("Broker (Broker atualmente inativo)")
		self.buttonStartBroker = QPushButton("Start Broker")
		vboxBroker = QVBoxLayout()
		vboxBroker.addWidget(self.labelBroker)
		vboxBroker.addWidget(self.buttonStartBroker)

		labelListMessage = QLabel("Mensagens que estão atualmente na fila:")
		self.listMessage = QListWidget()

		hboxAPIBroker = QHBoxLayout()
		hboxAPIBroker.addLayout(vboxAPI)
		hboxAPIBroker.addLayout(vboxBroker)

		vboxAll = QVBoxLayout()
		vboxAll.addLayout(hboxAPIBroker)
		vboxAll.addWidget(labelListMessage)
		vboxAll.addWidget(self.listMessage)


		self.connect(self.buttonStartAPI, SIGNAL("clicked()"), self.start_api)
		self.setLayout(vboxAll)
		self.setWindowTitle("Message Broker")
		self.setGeometry(300,100,700,430)


	def start_api(self):
		self.api = APIServer()
		self.api.start()
		self.labelAPI.setText("API Rest (ativo)")


app = QApplication(sys.argv)
dlg = index()
dlg.exec_()