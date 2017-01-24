#No. 02 - implement a Stack

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def top(self):
         return self.items[self.size()-1]
     def size(self):
         return len(self.items)

a = Stack()

a.push(4)
a.push(5)
a.push(6)
a.push(7)

print a.size()
print a.top()
print a.top()
print a.pop()
print a.pop()
print a.pop()
print a.pop()
print a.size()