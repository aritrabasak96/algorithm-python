# graph data structure----

class Graph:
    def __init__(self):
        pass

    def printNode(self,graph):

        for node,nodes in graph.items():
            print(nodes)

    def neighbourNode(self,node,graph):

        foundstatus = 0
        for allnode in graph:

            if node == allnode:
                print(graph[node])
                foundstatus = 1;

        if foundstatus is not 0:
            pass
        else:
            print("the node is not found in the graph")

if __name__ == "__main__":
    # create the Graph
    graph = {
       'A': ['B','C'],
       'B': ['A','C','D','E'],
       'C': ['A','B','D'],
       'D': ['C','B','E'],
       'E': ['B','D']
    }

    g = Graph();
    g.neighbourNode('B',graph);
