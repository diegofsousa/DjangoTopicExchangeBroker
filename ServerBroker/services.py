from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
import sys
from inicializador import start, stop
import pika
import sys

class APIServer(QThread):
	def __init__ (self, parent=None):
		QThread.__init__(self)		

	def run(self):	
		start()
		self.emit(SIGNAL("ip(QString)"), LOCAL_IP)

	def stopserver(self):
		stop()
		print("Parando servidor")


class RequestLogs(QThread):
	def __init__ (self, guiList, labelNum, parent=None):
		self.guiList = guiList
		self.labelNum = labelNum
		QThread.__init__(self)
		self.num = 0	

	def run(self):	
		connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
		channel = connection.channel()

		channel.exchange_declare(exchange='topic_logs',
		                         type='topic')

		result = channel.queue_declare(exclusive=True)
		queue_name = result.method.queue

		channel.queue_bind(exchange='topic_logs',
		                   queue=queue_name,
		                   routing_key='#')

		print(' [*] Waiting for logs. To exit press CTRL+C')

		def callback(ch, method, properties, body):
			item = QListWidgetItem("Topic: "+method.routing_key+" - Mensagem: "+body.decode("utf-8"))

			self.guiList.addItem(item)
			self.num += 1
			self.labelNum.setText("Numero de mensagens processadas: "+str(self.num))

			print(" [x] {} - {}".format(method.routing_key, body.decode("utf-8")))

		channel.basic_consume(callback,
		                      queue=queue_name,
		                      no_ack=True)

		channel.start_consuming()

	def list_clear(self):
		self.num = 0
