from queue import Queuep

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class AVLTree:
    def __init__(self):
        self.root = None


    # append data to the tree
    def append(self,data):
        temp = self.root
        parent = None
        add_node = Node(data)
        level_left = 0
        level_right = 0



        # if there is no data in the tree
        if self.root is  None:
            self.root = add_node
        # then there is already some data in the tree
        else:

            while temp is not None:
                parent = temp
                if temp.data < data:
                    temp = temp.next
                    level_right = level_right + 1

                elif temp.data > data:
                   temp = temp.prev
                   level_left = level_left + 1

            # now you get the last node where you need to place your node

            if parent.data < data:
                parent.next = add_node
            else:
                parent.prev = add_node

            this.rotation()
    # node_level
    def rotation(self):





    # print list
    def printlist(self):
        temp = self.root
        if self.root is None:
            print("no data in the tree")
        else:

            # level order search
            que = Queuep()
            que.push(temp)
            while(que.isEmpty() != -1):
                data = que.pop()
                print(data.data)
                if data.prev is not None:
                   que.push(data.prev)
                if data.next is not None:
                   que.push(data.next)

if __name__ == "__main__":
    avltree = AVLTree()
    avltree.append(30)
    avltree.append(20)
    avltree.append(40)
    avltree.append(60)
    avltree.append(70)
    avltree.append(80)

    avltree.printlist()
