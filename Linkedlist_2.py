# create a node class
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

# crete the linked list class

class Linkedlist:
    def __init__(self):
        self.head = None

    def appendDataatTheLast(self,data):

        new_node = Node(data) # create object of node
        if self.head is None:
            self.head = new_node

        else:
            last_node = self.head
            # find the last node
            while last_node.next is not None: # loop will terminate when it get none value
                last_node = last_node.next
            last_node.next = new_node


    # find the after node data value

    def aftervalue(self,data):
        x = data
        p = self.head
        while p is not None:
            if p.data == x:
                break
            p = p.next
        print(p.next.data)

    # find previous data

    def beforevalue(self,data):
        x = data
        p = self.head
        while p is not None:
            if p.next.data == x:
                break
            p = p.next # pointing to the same node
        print("before value",p.data)

    # add data in the given position
    def addValueAtaGivenposition(self,position,nodedata):

          p = self.head
          if position == 1:
              addnode = Node(nodedata)
              addnode.next = p.next
              self.head = addnode



          value = 1;
          addnode = Node(nodedata)

          while value< position-1 and p is not None:

              p = p.next
              value += 1
          if p is None:
              print("enter valid range")
          else:
            addnode.next = p.next
            p.next = addnode


    # delete mode from the linkedlist

    def delete(self,datavalue):

        x = datavalue
        value = 1;
        p = self.head
        while p is not None:
            if value == x:
                break
            p = p.next

        temp = p.next
        p.next = temp.next
   # find the data is in the list or not ???
    def findData(self,data):
        x = data
        location = 0
        position = self.head
        while position is not None:
            location += 1
            if position.data == x:
                print("found at location no ",location)
                break
            position = position.next

   # find the number of nodes is in the list or # NOt



    def numberofItem(self):
        n = 0
        node = self.head
        if self.head is None:
            print("there is no data yet")
        else:
            while node is not None:
                n += 1
                node = node.next
        print("total number of data is ",n)

    def appendDataatTheFirst(self,data):

        if self.head is None:
            print("there is no data yet")
        else:
            new_node = Node(data)
            pointingnode = self.head
            self.head = new_node
            new_node.next = pointingnode

    def printAllList(self):

        printlist = self.head
        while printlist is not None:
            print(printlist.data)
            printlist = printlist.next
        print("last node",printlist.data)

linkedlist = Linkedlist()
linkedlist.appendDataatTheLast("aritra")
linkedlist.appendDataatTheLast("debesh")
linkedlist.appendDataatTheLast("souvik")
linkedlist.appendDataatTheLast("rahul")

#linkedlist.printAllList()
