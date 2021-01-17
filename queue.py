# queue data structure
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queuep:
    def __init__(self):

        self.front = None
        self.rear = None
        self.root = None

    def push(self,data):
        add_node = Node(data)
        if self.root is None:
            self.root = add_node
            self.front = self.root
            self.rear = self.root
        else:
            temp = self.root
            while temp.next is not None:
                temp = temp.next
            temp.next = add_node
            self.rear = temp.next

    def pop(self):
        if self.root is None:
            print("no data in the list")
        else:
            temp = self.root
            data = self.root.data
            self.root = None
            self.root = temp.next
            self.front = self.root
            return data

    def isEmpty(self):
        temp = self.root
        if temp is not None:
            return 1
        else:
            return -1

    def printalldata(self):
        temp = self.root
        if temp:
          while temp is not None:
             print(temp.data)
             temp = temp.next
        else:
            print("no data in the list")



if __name__ == "__main__":
  q = Queuep()
  q.push(10)
  q.push(12)
  q.push(14)
  q.push(17)
  q.push(19)

  s1 = q.pop()
  #print(s1)
  s2 =q.pop()
  #print(s2)
  s3 = q.pop()
  #print(s3)
  e1 = q.isEmpty()
  print(e1)

  s4 = q.pop()
  s5 = q.pop()
  s6 = q.pop()

  e2 = q.isEmpty()
  print(e2)

  #print("print data")
  #q.printalldata()
create a queue
