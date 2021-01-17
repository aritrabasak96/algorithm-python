# Doubly linkedlist is very similar to linkedlist
# we have two pointer in node class = 1) next 2) previous

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Doublylinkedlist:
     def __init__(self):
         self.head = None

   # append data at the last
     def appenddataAtLast(self,data):
         new_node = Node(data)

         if self.head is None:
             self.head = new_node
             new_node.prev = None
         else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
            new_node.next = None

   # append data at the first
     def appendfirst(self,data):
         if self.head is None:
             print("list is empty")

         else:
             new_node = Node(data)
             tempo = self.head

             self.head = new_node
             new_node.next = tempo
             tempo.prev = new_node
    # how many data/nodes
     def count(self):
        if self.head is None:
            print("list is empty")
        else:
            temp = self.head
            count = 0
            while temp is not None:
                temp = temp.next
                count = count+1
            print(count)
    #find data in the node

     def found(self):
         temp = self.head
         count = 0
         while temp is not None:
             count = count+1
             temp = temp.next
         return count



     def findData(self,data):
          if self.head is None:
              print("list is empty")

          else:
              temp = self.head
              position = 0
              while temp is not None:
                  position = position+1
                  if(temp.data == data):
                      print(data,"found at position number",position)
                      break
                  temp = temp.next
              value = self.found()
                     # bug => can not find the last position
              if position >= value:
                  print(data,"not found")

   # add element at a given location
     def addNodeatPosition(self,position,data):

        temp = self.head
        new_node = Node(data)
        if position == 1:
            self.head = new_node
            new_node.next = temp
            temp.prev = new_node

        else:
            i = 1 # starting position is 1
            while i < position-1 and temp is not None:
                 i = i+1
                 temp = temp.next
            pointing = temp.next
            temp.next = new_node
            new_node.prev = temp
            new_node.next = pointing
            pointing.prev = new_node


     def printdata(self):
         temp = self.head
         while temp is not None:
             print(temp.data)
             temp = temp.next

doubly = Doublylinkedlist()
doubly.appenddataAtLast("aritra")
doubly.appenddataAtLast("debesh")
doubly.appenddataAtLast("mrinal")
doubly.appenddataAtLast("souvik")
doubly.appenddataAtLast("rahul")
doubly.addNodeatPosition(2,"dibu")

doubly.printdata()



doubly.findData("sou")
