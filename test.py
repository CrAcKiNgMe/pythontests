
import os

import threading
import  Queue

q = Queue.Queue()

q.put(1234,False)
q.put(2,False)
q.put(3,False)
q.put(4,False)
q.put(5,False)

print q.qsize()
print q.get(False)
print q.get(False)
print q.get(False)
print q.get(False)
print q.get(False)

print q.qsize()

def foo():
    a = 5
    if(a > 5):
        print "a>5"
        print "foo**********************************"
    else:
        print "a <= 5";
        print "hahha"

a = [1,2,3,4,5]

print "********************"
for iter in a:
    if(iter == 1):
        a.remove(3)
    print iter

print "********************"

class base():
    pass

a = base()


from anytree import Node, RenderTree
udo = Node("Udo")
marc = Node("Marc", parent=udo)
lian = Node("Lian", parent=marc)
dan = Node("Dan", parent=udo)
jet = Node("Jet", parent=dan)
jan = Node("Jan", parent=dan)
joe = Node("Joe", parent=dan)

print udo

for pre, fill, node in RenderTree(udo):
    print("%s%s" % (pre, node.name))

seq_a = list("helao")#list
seq_a2 = [1,2,3,5]  #list




seq_b = "heelo"#str
seq_b2 = str("12345")#str

seq_b3=seq_b.upper();

print seq_b3

seq_c = unicode("134")#unicode
seq_c2 = unicode(seq_b2)


seq_d = tuple('abc') #(tuple[1,2,3])
seq_d2 = tuple([1,3,4])


seq_e = bytearray(seq_d)



print type(seq_a)

print type(seq_a2)
print type(seq_b)
print type(seq_b2)
print type(seq_c2)
print seq_c2
print type(seq_d)
print seq_d
print seq_d2

print type(seq_e)


d = xrange(0, 10,2)
print type(d)
print d


e = range(0, 10,2)
print type(e)
print e