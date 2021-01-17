#from queue import Queuep
from stack import Stack
import operator
class Vertex:
    def __init__(self,data):
        self.data = data
        self.color = "black"
        self.stackVisited = "black"
        self.adjacent = {}
        self.inQueue = "N"

    def addNeighbor(self,node,weight=1):
        self.adjacent[node] = weight



class Graph:

    def __init__(self):
        self.graph = {}

    def addVertex(self,vertex):
        ver = Vertex(vertex)
        self.graph[vertex] = ver # store the address of each vertex

    def addWeight(self,frm,to,weight):
        self.graph[frm].addNeighbor(self.graph[to],weight)

    def findNeighbor(self,vertex):
        for key in self.graph: # travers through each key in the dict
            if(vertex == key): # find the vertex you want
                val = self.graph[vertex]  # if you find ... find its value ex: abc = {key:value}
                for k in val.adjacent: # return the vertext instances, travers through it
                    print(k.data) # print its data




    def printGraphBreadh(self,vertex):
       # breadth first search
        que = Queuep()

        # start traversal from the first node
        for key in self.graph: # the vertex is in the graph or not
            if(vertex == key):  # if you find the vertext
                que.push(vertex)  # push the vertex ex: {a:vertex,b:vertex}

                while(que.isEmpty() != -1):
                    node = que.pop() # pop the first vertex {a}

                    ver = self.graph[node] # take its vertixes ## val == node

                    print(ver.data) # print the vertex
                    ver.color = "red" # change the vertex color to red... that mean the node/vertex is already visited
                    for k in ver.adjacent:
                        if k.color is not "red" and k.inQueue is "N": # if the vertex color is not red and if the vertex is not in the queue
                           que.push(k.data)
                           k.inQueue = "Y"  # if the vertex is already in the queue



    def printGraphDepth(self,vertex):

        sta = Stack()
        value = vertex
        maxval = ""


        for k in self.graph:
            if(value == k): # if the value that you enter is in the list
                sta.push(value) # push the vertex in the stack
                while(sta.isEmpty() != -1):

                    popvertex = 0
                    ver = self.graph[value]
                    ver.stackVisited = "blue" # mark the vertex blue(in the stack)

                    for k in ver.adjacent: # travers its neighbors
                        if k.stackVisited is not "blue" and k.color is not "red": # if its neighbors are not in the stack(not blue)
                            if(maxval < k.data):
                               tempvertex = k # find the maximum value
                               popvertex = 1
                    if(popvertex == 0): # if all its neighbors are blue that means the node/vertex is the last
                        val = sta.pop() # pop that vertex
                        print(val[0])
                        if val[1] is not None:
                            value = val[1].data # point the next value of the stack to 'value' variable
                    else:
                      sta.push(tempvertex.data) # otherwise push the vertex in the stack
                      value = tempvertex.data


if __name__ == "__main__":

    g = Graph()
    g.addVertex('A')
    g.addVertex('B')
    g.addVertex('C')
    g.addVertex('D')
    g.addVertex('E')
    g.addVertex('F')
    g.addVertex('G')

    g.addWeight('A','B',5)
    g.addWeight('B','A',6)
    g.addWeight('A','C',4)
    g.addWeight('C','A',5)
    g.addWeight('B','D',9)
    g.addWeight('D','B',5)
    g.addWeight('C','D',2)
    g.addWeight('D','C',5)
    g.addWeight('D','G',8)
    g.addWeight('G','D',5)
    g.addWeight('D','E',3)
    g.addWeight('E','D',5)
    g.addWeight('D','F',1)
    g.addWeight('F','D',5)

    g.printGraphDepth('A')
