#Stack Definition

#Data structure - LILO(Last In First Out)
#Functionality

    #Needed for current problem
    
    #push - add an item to the top of the stack
    #pop - remove an item from the top of the stack

    #Extras

    #top - shows the top item on the stack
    #size - returns the size of the stack
    #empty - returns true if the stack is empty

    #Stack will use a list

class Stack:

    def __init__(self):
        self.stack = []

    #Pushes the value spcified by 'item' onto the top of the stack
    def push(self, item):
        self.stack.append(item)

    #Removes the top element on the stack and returns its value
    def pop(self):
        if(not self.isEmpty()):
            return self.stack.pop(self.size() - 1)

    def reverseStack(self):
        self.stack.reverse()

    #returns the current size of the stack
    def size(self):
        return len(self.stack)

    #prints the content of the stack    
    def printStack(self):
        print(self.stack)

    #check to see if the stack is empty or not
    def isEmpty(self):
        return self.size() <= 0

    #prints the length and elements in the stack
    def printInfo(self):
        print("stackLength: " + str(self.size()))
        print(self.stack())


"""
TESTS

Some basic tests, these are by no means comprehensive 

test = Stack()

#test 1 - printing the stack
test.printStack()
print(test.size())

#test 2 - pushing items to the stack
test.push("first Append")
test.push("second Append")
test.printStack()
print(test.size())

#test 3 - removing items from the stack
p1 = test.pop()
p2 = test.pop()
print(p1)
print(p2)
test.printStack()
print(test.size())

#test 5 - checking if the stack is empty
test.pop()
test.pop()
test.printStack()
print(test.isEmpty())
"""

