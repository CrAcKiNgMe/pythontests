import os
import Queue


class Node:

    def __init__(self,value):
      self.left = None
      self.right = None
      self.value = value

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid
    def pre_order(self):
        print self.value
        if(self.left):self.left.pre_order()
        if(self.right):self.right.pre_order()
    def in_order(self):
        if(self.left):self.left.in_order()
        print self.value
        if(self.right):self.right.in_order()
    def post_order(self):
        if(self.left):self.left.post_order()
        if(self.right):self.right.post_order()
        print self.value

    def level_order(self):
        q = Queue.Queue()
        q.put(self);
        while (q.qsize() > 0):
            tmp = q.get()
            print tmp.value
            if(tmp.left): q.put(tmp.left)
            if(tmp.right): q.put(tmp.right)




btree = Node("A")
btree.left = Node("B")
btree.right = Node("C")
btree.left.left = Node("D")
btree.left.right = Node("E")
btree.right.left   = Node("F")
#btree.right.right  = Node("6")
#btree.right.right.left  = Node("7")


btree.level_order()






