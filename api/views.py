from rest_framework.response import Response
from rest_framework.views import APIView

class ReadRoot(APIView):
    def get(self,req):
        return Response({'Ping': 'Pong'})

class ParsePipelineView(APIView):
    def dfsCheck(self, node, adj, visited, pathVisited):
        visited[node] = 1
        pathVisited[node] = 1
        
        for neighbor in adj[node]:
            if visited[neighbor] == 0:
                if self.dfsCheck(neighbor, adj, visited, pathVisited) == True:
                    return True
            elif pathVisited[neighbor] == 1:
                return True

        pathVisited[node] = 0
        return False

    def post(self,req):
        nodes,edges = req.data.values()
        nodeSet = set()
        edgeSet = set()
        
        for edge in edges:
            nodeSet.add(edge['source'])
            nodeSet.add(edge['target'])
        
        for edge in edges:
            edge_key = (edge['source'], edge['target'])
            edgeSet.add(edge_key)
        
        adj = {}
        for node in nodeSet:
            adj[node] = set()
        
        for source, target in edgeSet:
            adj[source].add(target)
        
        print(adj)
        
        visited = {}
        pathVisited = {}
        for node in adj:
            visited[node] = 0
            pathVisited[node] = 0
        
        is_cyclic = False
        for node in visited:
            if visited[node] == 0:
                if self.dfsCheck(node, adj, visited, pathVisited) == True:
                    is_cyclic = True
                    break
        
        is_dag = not is_cyclic
        
        print(visited)
        return Response({'num_nodes': len(nodeSet), 'num_edges': len(edgeSet), "is_dag": is_dag})