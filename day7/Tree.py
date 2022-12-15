#Rooted Tree with unbounded branching

#A tree has a root
#contains branches
#each branch ends in a node
#each node can contain other branches

class Tree:
    #A tree must have a root
    def __init__(self, root):
        self.root = root
        self.treeSize = 0
    
    def printRoot(self):
        content = self.root.getContent()
        print(content)
        print(self.root.children[0].getContent())

    def findNode(self, node):
        return None
        

    #functionality

    #Must be able to add a node

    #Creates a new node that points to the parent node given
    #and contains the information given in content
    #increments the number of tree edges by 1
    def addChild(self, parent, content):
        node = Node(parent, content)
        parent.addChild(node)
        self.treeSize += 1
    
    #Must be able to remove a node

    #Count the amount of nodes in the tree

    #Search the tree for a specfic node

    
    
class Node:
    #Each node must have a parent except for the root node
    #Each node can have 0 or more children

    def __init__(self, parent, content):
        self.parent = parent
        self.content = content
        self.children = []

    def getContent(self):
        return self.content

    def addChild(self, child):
        self.children.append(child)
        

    #Must be able to add a children to the node


