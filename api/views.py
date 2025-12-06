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
        edgeSet = set()
        for edge in edges:
            nodeSet.add(edge['source'])
            nodeSet.add(edge['target'])
        # to avoid duplicate edges
        for edge in edges:
            edge_key = (edge['source'], edge['target'])
            edgeSet.add(edge_key)
        
        # creating adjacency list
        adj = {}
        for node in nodeSet:
            adj[node] = set()
        for source,target in edgeSet:
            if source not in adj:
                adj[source] = set()
            adj[source].add(target)
        print(adj)

        return Response({'number of nodes': len(nodeSet), 'number of edges': len(edgeSet)})