from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class ReadRoot(APIView):
    def get(self,req):
        return Response({'Ping': 'Pong'})

class ParsePipelineView(APIView):
    def post(self,req):
        return Response({'status': 'parsed'})