#circular linkedlist
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Circularlinkedlist:
    def __init__(self):
        self.head = None

    # append data
    def append(self,data):
        new_node = Node(data)
        temp = self.head
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    # prepend data
    def prepend(self,data):
        if self.head is None:
            print("there is no data")
        else:
            new_node = Node(data)
            temp = self.head
            var = self.head
            # check if there is  only one node in the list or not
            if temp == temp.next:
                self.head = new_node
                new_node.next = temp
                temp.next = new_node
            # for more than one node in the list
            else:
               while temp.next != self.head:
                   temp = temp.next
               self.head = new_node
               new_node.next = var
               temp.next = new_node

    # print data
    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
            if temp == self.head:
                 # there is no None value,so you have to write this condition
                break


circular = Circularlinkedlist()
circular.append("aritra")
circular.append("debesh")
circular.append("rahul")
circular.prepend("souvik")

circular.printlist()
