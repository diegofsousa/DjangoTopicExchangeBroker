from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys, os, subprocess
import netifaces

from services import APIServer, RequestLogs


class index(QDialog):
	def __init__(self, parent=None):
		super(index, self).__init__(parent)
		self.api = APIServer()
		
		self.labelAPI = QLabel("API Rest (Rest atualmente inativo)")
		self.buttonStartAPI = QPushButton("Start Rest")
		vboxAPI = QVBoxLayout()
		vboxAPI.addWidget(self.labelAPI)
		vboxAPI.addWidget(self.buttonStartAPI)

		self.labelBroker = QLabel("Numero de mensagens processadas: 0")
		self.buttonStartBroker = QPushButton("Limpar mensagens")
		vboxBroker = QVBoxLayout()
		vboxBroker.addWidget(self.labelBroker)
		vboxBroker.addWidget(self.buttonStartBroker)

		labelListMessage = QLabel("Mensagens que estão atualmente na fila:")
		self.listMessage = QListWidget()
		self.logs = RequestLogs(self.listMessage, self.labelBroker)

		hboxAPIBroker = QHBoxLayout()
		hboxAPIBroker.addLayout(vboxAPI)
		hboxAPIBroker.addLayout(vboxBroker)

		vboxAll = QVBoxLayout()
		vboxAll.addLayout(hboxAPIBroker)
		vboxAll.addWidget(labelListMessage)
		vboxAll.addWidget(self.listMessage)


		self.connect(self.buttonStartAPI, SIGNAL("clicked()"), self.start_api)
		self.connect(self.buttonStartBroker, SIGNAL("clicked()"), self.clean_messages)
		self.setLayout(vboxAll)
		self.setWindowTitle("Message Broker")
		self.setGeometry(300,100,700,430)


	def start_api(self):
		
		self.api.start()
		
		self.labelAPI.setText("API Rest (ativo)")
		

		LOCAL_IP = "Nothing"

		try:
			LOCAL_IP = netifaces.ifaddresses('wlan0')[2][0]['addr']
		except Exception as e:
			print('Interface Wifi não detectada')
		try:
			LOCAL_IP = netifaces.ifaddresses('eth0')[2][0]['addr']
		except Exception as e:
			print('Interface cabeada não detectada')
		self.buttonStartAPI.setEnabled(False)
		self.buttonStartAPI.setText("Running in " + LOCAL_IP)
		self.logs.start()

	def clean_messages(self):
		self.labelBroker.setText("Numero de mensagens processadas: 0")
		self.listMessage.clear()
		self.logs.list_clear()


app = QApplication(sys.argv)
dlg = index()
dlg.exec_()