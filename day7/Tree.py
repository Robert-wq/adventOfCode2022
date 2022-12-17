#Rooted Tree with unbounded branching

#A tree has a root
#contains branches
#each branch ends in a node
#each node can contain other branches

from Queue import *
from Stack import *

class Tree:
    #A tree must have a root
    def __init__(self, root):
        self.root = root
        self.treeSize = 0

    def findNode(self, node):
        return None
        
    def printTree(self):
        print(self.root.getContent())
        currentNode = self.root
        while currentNode.children:
            for node in currentNode.children:
                print(node.getContent())
            currentNode = currentNode.children[0]
        
    #functionality

    #Creates a new node that points to the parent node given
    #and contains the information given in content
    #increments the number of tree edges by 1
    def addChild(self, parent, content):
        node = Node(parent, content)
        parent.addChild(node)
        self.treeSize += 1
        return node
    
    #Must be able to remove a node
    #How
        #Find the node that needs to be removed
        #temporary store that nodes children
        #remove the node from the parents children list
        #add the temporary children to the parent

    #Count the amount of nodes in the tree

    #Search the tree for a specfic node


    #TODO, change this so that it actually seaches for something
    def breadthFirstSearch(self):
        visitedList = []
        toVisitQueue = Queue()

        root = self.root
        print(root.content)
        for child in root.children:
            toVisitQueue.enqueue(child)
        
        while not toVisitQueue.isEmpty():
            currentNode = toVisitQueue.dequeue()
            print(currentNode.getContent())
            for child in currentNode.children:
                toVisitQueue.enqueue(child)

    #TODO, change this so that it actually searches for something
    def depthFirstSeach(self):
        visitedList = []
        toVisitStack = Stack()

        root = self.root
        print(root.content)
        for child in root.children:
            toVisitStack.push(child)
        
        while not toVisitStack.isEmpty():
            currentNode = toVisitStack.pop()
            print(currentNode.getContent())
            for child in currentNode.children:
                toVisitStack.push(child)



    
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


