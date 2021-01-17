# Depth First Search algorithm using python
# you can create n nuumber of nodes
# and you can connect each nodes.
# its a weighted and undirected graph
# what data structure we use => adjacency list ds and stack
# ---------------------------------------------
# import stack
from stack import Stack
import random
# create a node/vertex 
class Vertex:

    def __init__(self,data=None):

        self.data = data  # vertex name 
        self.neighbor = {} # map the nodes A -> {B:2, C:3, D:6}
        self.visited = -1 # the vertex is not visited initially

    def addNeighbor(self,othervertex,weight): # the other nodes that you want to connect to this node/vertex

       self.neighbor[othervertex] = weight  

    

# create the main graph
class Graph:

    def __init__(self):
        self.graph = {}  # the main graph where we put all the vertex
        

    def addVertex(self,vertexName):
        # create the instance of the node
        ver = Vertex(vertexName) # ver is the instance variable which store the address of the newly create vertex
        self.graph[vertexName] = ver #  self.graph = {} => {vertexname : # address_of_the_new_node }

    def addWeight(self,frm,to,wt=1):
        self.graph[frm].addNeighbor(to,wt) # self.graph[frm] => is pointing to the address of the object in this graph
                                            # so you can call its method which is addNeighbor 
                                            # to = the next node in the graph 
                                            # frm = {to:wt}

    # find a vertex is present in the graph or not
    # caution: for worst case time complexity is O(V)
    def findVertex(self,vertexName):
        foundFlag = 0
        for key in self.graph:
            if(key == vertexName):
                 foundFlag = 1
        if foundFlag == 0:
            print('The vertex you try to find is not in the graph')
        elif foundFlag == 1:
            print('It is in the graph')

    
    # find there is any circle present or not
    def findCircle(self,vertex):
        parent = {} # this will keep track of every adjacent vertex
        stack = Stack()
        value = vertex
        circle = None
        # start from any node and put it in the stack
        try:
           startnode = self.graph[vertex]
        except KeyError:   
            return 'the vertex is not in the graph'     
        else:
           
            stack.push(startnode.data)
            parent[startnode.data] = None
            startnode.visited = 0
            track_cycle = []  

            while(stack.isEmpty() != -1):
                # stack_pop is parent
                stack_pop = self.graph[value]
               
                # ** to find its adjacent **
                mylist = []
                count = 0
                i = 0
                j = 0
                next_stack_value = None
                leaf_node = None # keep track that the node is leaf node or not 
               
                for k in stack_pop.neighbor:
                    mylist.append(k)  # the adjacent values are in the mylist
                    count = count +1
                # check its each adjacent vertex
                # 1. find how many vertex are in the mylist
               
                length_list = len(mylist) 
               
                while(i<=length_list-1):

                    random_value = random.randint(0,count-1)
                    i = i+1
                  
                    adjacent_vertex = mylist[random_value]
                    if self.graph[adjacent_vertex].visited != 0 and self.graph[adjacent_vertex].visited != 1:
                           next_stack_value = adjacent_vertex 
                           # maintain the child-parent relationship
                           parent[adjacent_vertex] = stack_pop.data

                           leaf_node = "No"  # the node is not a leaf node

                           break
                    else:
                        mylist.remove(adjacent_vertex)  
                        count = count - 1 # you remove a value from the list
                                           # so you have to decrease one valur from count 

                if  leaf_node == 'No': # the node is not visited
                     
                      stack.push(next_stack_value)
                      value = next_stack_value
                      self.graph[next_stack_value].visited = 0
                else: 
                    # what idf the stack_pop is the leaf node
                    pop = stack.pop()
                   
                    # pop == stack_pop
                    self.graph[pop].visited = 1
                    find_parent = parent[pop]
                   
                    #  ***** once you pop the value make sure that you change the 'value' to the value of prev value of stack
                    value = find_parent
                    # find its adjacent
                   
                    for y in self.graph[pop].neighbor:
                       
                        if y != find_parent:
                            
                            if self.graph[y].visited == 0:
                                circle = "found"
                                find_cycle_pattern = []
                                # we find cycle pattern pop -> y
                               
                                find_cycle_pattern.append(y)
                                find_cycle_pattern.append(pop)
                                  
                                temp_pop = pop  
                               
                                while(find_cycle_pattern.count(temp_pop) <= 1):
                                   
                                    previous_value =  parent[temp_pop]
                                    find_cycle_pattern.append(previous_value)
                                    temp_pop = previous_value
                                print("the cycle ->",find_cycle_pattern)    
                               
                # while loop closed
                  
            if circle == 'found':
               
                return "there is a cycle in the graph"
            else:
                
                return "there is NO cycle in the graph"               
                           

    def findBridge(self):
        pass

    

if __name__ == "__main__":
     # create a graph
     graph = Graph()
     graph.addVertex('A')
     graph.addVertex('B')
     graph.addVertex('C')
     graph.addVertex('D')
     graph.addVertex('E')
     graph.addVertex('F')
     graph.addVertex('G')
     graph.addVertex('H')
     graph.addVertex('I')


     graph.addWeight('A','B',2)
     graph.addWeight('B','A',2)
     graph.addWeight('A','H')
     graph.addWeight('H','A',2)
     graph.addWeight('H','I',2)
     graph.addWeight('I','H',2)
     graph.addWeight('B','D',2)
     graph.addWeight('D','B',2)
     graph.addWeight('D','E',7)
     graph.addWeight('E','D',2)
     graph.addWeight('C','I',5)
     graph.addWeight('I','C',2)
     graph.addWeight('I','F',5)
     graph.addWeight('F','I',2)
     graph.addWeight('I','G',5)
     graph.addWeight('G','I',2)
     graph.addWeight('G','F',5)
     graph.addWeight('F','G',2)
     
     
    
     

     data = graph.findCircle('A')
     print(data)  
     
