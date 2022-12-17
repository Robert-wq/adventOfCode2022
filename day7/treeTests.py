from Tree import *

n = Node(None, "Home directory")
t = Tree(n)

c11 = t.addChild(n, "\tc11")
c12 = t.addChild(n, "\tc12")
c13 = t.addChild(n, "\tc13")

c2111 = t.addChild(c11, "\t\tc2111")
c2112 = t.addChild(c11, "\t\tc2112")
c2113 = t.addChild(c11, "\t\tc2113")

c2121 = t.addChild(c12, "\t\tc2121")
c2122 = t.addChild(c12, "\t\tc2122")
c2123 = t.addChild(c12, "\t\tc2123")

c21211 = t.addChild(c2121, "\t\t\tc21211")
c21212 = t.addChild(c2121, "\t\t\tc21212")
c21213 = t.addChild(c2121, "\t\t\tc21213")




#t.printTree()
print("Breadth First Search")
t.breadthFirstSearch()

print("\n\nDepth First Search")
t.depthFirstSeach()


