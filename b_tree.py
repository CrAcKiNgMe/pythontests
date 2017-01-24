#No. 04 - all possible path from root to leaf

import Queue

q = []
qq = []


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def enumpath(self):
        q.append(self.value)

        if(not (self.left) and not(self.right)):
            print q
        if(self.left):
            self.left.enumpath()
        if(self.right):
            self.right.enumpath()
        q.pop();


a = TreeNode("a")
a.left = TreeNode("b")
a.right = TreeNode("c")
a.left.left  = TreeNode("d")
a.left.right  = TreeNode("e")
a.right.left  = TreeNode("f")
a.right.right  = TreeNode("g")

a.enumpath()

print qq