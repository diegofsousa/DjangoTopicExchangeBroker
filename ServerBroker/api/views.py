from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ServerBroker.settings import LOCAL_IP
import pika
import sys


class StatusView(APIView):
	"""
	Esta API aceita como conteúdo do verbo POST a seguinte estrutura de objeto JSON:
	{
	     "mensagem": "Mensagem de exemplo",
	     "topic_exchange": "Aqui ficam os exchanges"
	}
	"""
	def get(self, request, format=None):
		return Response(LOCAL_IP)

	def post(self, request, format=None):
		try:
			connection = pika.BlockingConnection()
			channel = connection.channel()

			channel.exchange_declare(exchange='topic_logs',
			                         type='topic')

			channel.basic_publish(exchange='topic_logs',
			                      routing_key=request.data["topic_exchange"],
			                      body=request.data["mensagem"])
			print(" [x] Sent %r:%r" % (request.data["topic_exchange"], request.data["mensagem"]))
			connection.close()
			print("Mensagem recebida: {}".format(request.data["mensagem"]))
			print("Topico recebido: {}".format(request.data["topic_exchange"]))
		except Exception as e:
			print(e)
		
		return Response("request")