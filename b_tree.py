#No. 02 - implement a Stack wit minimize number

class Stack:
     def __init__(self):
         self.items = []
         self.min_items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         if(self.size() == 0):
             self.min_items.append(item)
         elif(item > self.min()):
             self.min_items.append(self.min())
         else:
             self.min_items.append(item)
         self.items.append(item)
     def pop(self):
         self.min_items.pop()
         return self.items.pop()

     def top(self):
         return self.items[self.size()-1]

     def min(self):
         return self.min_items[len(self.min_items) - 1]

     def size(self):
         return len(self.items)


class Stack2:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def top(self):
        return self.items[len(self.items) - 1]

    def push(self, item):
        if(self.size() == 0):
            self.items.append(item)
            self.min  = item
        elif(item > self.min):
            self.items.append(item)
        else:
            self.items.append(2 * item - self.min)
            self.min = item
    def pop(self):
        if(self.min < self.top()):
            return self.items.pop()
        else:
            tmp = self.min
            self.min = self.min * 2 - self.top()
            self.items.pop()
            return  tmp

    def minnum(self):
        return self.min

    def content(self):
        print self.items

s = Stack2()

s.push(88)
s.push(89)
s.push(90)
s.push(1)



print s.content(), s.minnum()
s.pop()
print s.content(), s.minnum()
s.pop()
print s.content(), s.minnum()
s.pop()
print s.content(), s.minnum()
s.pop()

