from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ServerBroker.settings import LOCAL_IP

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
		print("Mensagem recebida: {}".format(request.data["mensagem"]))
		print("Topico recebido: {}".format(request.data["topic_exchange"]))
		return Response("request")