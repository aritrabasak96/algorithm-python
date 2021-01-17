# binary tree data structure
from queue import Queuep
class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class Binarytree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        add_node = Node(value)

        if self.root is None:
            self.root = add_node
        else:
            parent = None
            temp = self.root
            while temp:
                parent = temp
                if temp.data <= value:
                    temp = temp.next
                else:
                    temp = temp.prev
            if parent.data <= value:
                parent.next = add_node
            else:
                parent.prev = add_node

# to print the data -> 1) pre-order 2) in-order 3) post-order

# use pre-order first
    def preorder(self,root):
          if(root is not None):
               print(root.data)
               self.preorder(root.prev)
               self.preorder(root.next)

    def printtreepreorder(self):
          root = self.root
          self.preorder(root)
# use in-order
    def inorder(self,root):
        if(root is not None):

            self.inorder(root.prev)
            print(root.data)
            self.inorder(root.next)

    def printinorder(self):
        root = self.root
        self.inorder(root)

# use post-order
    def postorder(self,root):
        if(root is not None):

            self.postorder(root.prev)
            self.postorder(root.next)
            print(root.data)

    def printpostorder(self):
        root = self.root
        self.postorder(root)


# level order traversal
    def levelorderserach(self):
         que = Queuep()
         temp = self.root
         if temp is None:
             print("tree is empty")
         else:
           que.push(temp)
           while(que.isEmpty() != -1):
              data = que.pop()
              print(data.data)
              if data.prev is not None:
                 que.push(data.prev)
              if data.next is not None:
                 que.push(data.next)

# search a node
    def searchdata(self,data):
        temp = self.root
        level = 0
        value = 0

        while temp is not None:
            level = level +1
            if temp.data == data:
                print(data,"is found in the",level,"th level")
                value = 1
                break
            else:
                if temp.data < data:
                    temp = temp.next
                elif temp.data > data:
                    temp = temp.prev
        if value != 0:
            pass
        else:
            print("data is not found")

# balance factor

    def balancefactor(self):
        tempa = self.root
        tempb = self.root
        left_level = 0
        right_level = 0

        while tempa is not None:
            left_level = left_level+1
            if tempa.prev is not None:
                tempa = tempa.prev

        while tempb is not None:
            right_level = right_level+1
            if tempb.next is not None:
                tempb = tempb.next

        data = left_level - right_level
        if data == 0 or data == 1 or data == -1:
            print("tree is ordered")
        else:
            print("tree is unordered")


# delete tree

    def deletenode(self,deletedata):
        # first find the node/data
        parent = None
        temp = self.root
        while temp and temp.data != deletedata:
            parent = temp

            if temp.data < deletedata:
                    temp = temp.next
            elif temp.data > deletedata:
                    temp = temp.prev
        if temp is None or temp.data != deletedata:
            print("the data you are trying to delete is not found")
        # now if the node has no children
        else:
         ### temp is the node that you want to delete
         ### Parent is pointing to the node

          if temp.prev is None and temp.next is None:
               if parent.prev == temp: # or deletedata < parent.data then parent.prev = None
                  parent.prev = None
               elif parent.next == temp:
                  parent.next = None
        # if the node has left child
          if temp.prev is not None and temp.next is None:
               temporary = temp.prev
               temp.prev = None
               parent.prev = temporary
        # if the node has right child
          if temp.next is not None and temp.prev is None:
               temporary = temp.next
               temp = None
               parent.next = temporary
        # if the node has both children ( we target the right side)
          if temp.next is not None and temp.prev is not None:
              Parent_lastnode = None
              nextnode = temp.next # nextnode = 42, temp = 40 ( delete), parent = 35

              if nextnode.next is None and nextnode.prev is None: # is is the leaf node
                  if parent.next == temp:
                      temp.data = nextnode.data
                      temp.next = None
                  elif parent.prev == temp:
                       temp.data = nextnode.data
                       temp.next = None
              if nextnode.next is not None and nextnode.prev is None: # if it has right child only
                        lastnode = nextnode.next
                        temp.data = nextnode.data
                        temp.next = lastnode

              if nextnode.next is None and nextnode.prev is not None: # if it has left child only
                    lastnode = nextnode.prev
                    temp.data = lastnode.data
                    nextnode.prev = None

              if nextnode.next is not None and nextnode.prev is not None: #if it has both child
                    while nextnode.prev is not None:
                         Parent_lastnode = nextnode
                         if nextnode is not None:
                             nextnode = nextnode.prev
                         else:
                            break
                    temp.data = nextnode.data
                    Parent_lastnode.prev = None





# data entry

binarytree = Binarytree()
binarytree.insert(30)
binarytree.insert(20)
binarytree.insert(35)
# binarytree.insert(14)
# binarytree.insert(27)
# binarytree.insert(34)
# binarytree.insert(40)
# binarytree.insert(31)
# binarytree.insert(38)
# binarytree.insert(42)
# binarytree.insert(36)
# binarytree.insert(39)
# binarytree.insert(41)
#binarytree.insert(47)


# binarytree.levelorderserach()
# binarytree.deletenode(34)
#
# print("  ")
#
# binarytree.levelorderserach()

binarytree.balancefactor()
