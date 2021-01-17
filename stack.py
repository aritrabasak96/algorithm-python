class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.front = None
        self.root = None

    def push(self,data):
        node = Node(data)

        if self.root is None: # if there is no data in the stack

            self.root  = node
            self.front = self.root
        else:
            temp = self.root
            while temp.next is not None:
                temp = temp.next
            #we get the last node in temp
            temp.next = node
            self.front = temp.next

    def pop(self):

        if self.root is None:
            print("no data in the stack")
        else:

            temp = self.root # first data in the stack
            data = self.front.data # top most data in the stack => self.front points to the top most node in the stack
            popnode_prev = None # create a variable
            while temp is not None and temp.data != data: # our goal is to reach the top
                popnode_prev = temp # get the previous node of the top most node in the stack
                temp = temp.next


            if self.front == self.root: # when the last node remaining in the stack
               self.front = None
               self.root = None
            else: # otherwise
              popnode_prev.next = None
              self.front = popnode_prev


            return data

    def isEmpty(self):
        temp = self.root
        if temp is not None:
            return 1
        else:
            return -1


if __name__ == "__main__":

    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(50)
    s.push(70)


    while(s.isEmpty() != -1):
        data = s.pop()
        print("data",data)
        # if data[1] is not None:
        #     print("point to",data[1].data)
