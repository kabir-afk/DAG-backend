from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class ReadRoot(APIView):
    def get(self,req):
        return Response({'Ping': 'Pong'})

class ParsePipelineView(APIView):
    def post(self,req):
        nodes,edges = req.data.values()
        # for calculating total number of nodes
        nodeSet = set()
        for edge in edges:
            nodeSet.add(edge['source'])
            nodeSet.add(edge['target'])
        return Response({'number of nodes': len(nodeSet),'number of edges': len(edges)})