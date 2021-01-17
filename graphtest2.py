# first create the vertex
class Vertex:

    def __init__(self,data):
        self.data = data
        self.adjacent = {}

    def addNeighbor(self,node,weight=0):
        self.adjacent[node] = weight

    def findNeighbor(self,node):
        if node in self.adjacent:
            print(self.adjacent[node])


class Graph:
    def __init__(self):

        self.newvertex = None
        self.dict = {}

    def addVertex(self,data):

        self.newvertex = Vertex(data)
        self.dict[data] = self.newvertex

    def addEdge(self,frm,to,cost=0):

        self.dict[frm].addNeighbor(self.dict[to],cost)


    def printVertex(self):

        for vertex in self.dict:
            print(vertex)

    def neg(self,value):
        self.newvertex.findNeighbor(value)

graph = Graph()
graph.addVertex('a')
graph.addVertex('b')
graph.addVertex('c')
graph.addVertex('d')

graph.addEdge('a','b',3)

graph.neg('a')
