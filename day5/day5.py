from Stack import Stack

stacks = []

def createStacks(stacks):
    #create a list of 9 stacks
    for i in range(0, 9):
        stack = Stack()
        stacks.append(stack)

#Cycles through each line of the map
#If a letter is present in the map it appears every 4 characters
#This checks to see if that letter is present
def addLineToStacks(line):
    columnNumber = 0
    for i in range(0, len(line)):  
        if(i % 4 == 1):
            columnNumber += 1
            if(line[i] != " "):
                stacks[columnNumber - 1].push(line[i])  


createStacks(stacks)

with open("input.txt", 'r') as f:

    #Allows for the counting of lines within the file
    lineCounter = 0

    for line in f:
        #Gets the first 9 lines which contain the map
        if(lineCounter < 8):
            #adds the letters from the current line to the correct stack
            addLineToStacks(line)

        #increments the line count    
        lineCounter += 1
    
    #When i created the stacks i pushed all of the items on which meant i had to flip the stack
    #to make sure the letetrs where in the correct position. 
    #There is definately a better way to accomplish this but i wanted to create a stack in Python aswell
    #as complete this challenge so i made it work.
    for stack in stacks:
        stack.reverseStack()

for j in stacks:
    j.printStack()

print("\n")


def moveOneAtATime(line):
    splitLine = line.split()

    #Removes the needed numbers from the split line
    #1 is subtracted here due to the zero based index of the stack
    amountToMove = int(splitLine[1])
    columnToRemoveFrom = int(splitLine[3]) - 1
    columnToAddTo = int(splitLine[5]) - 1

    #pops each number off the top of the stack and adds it to the new stack
    for i in range(amountToMove):
        item = stacks[columnToRemoveFrom].pop()
        stacks[columnToAddTo].push(item)

def moveMultiple(line):
    #push the creates to a temporary stack
    #pop the creates back onto the new stack
    splitLine = line.split()

    #Removes the needed numbers from the split line
    #1 is subtracted here due to the zero based index of the stack
    amountToMove = int(splitLine[1])
    columnToRemoveFrom = int(splitLine[3]) - 1
    columnToAddTo = int(splitLine[5]) - 1

    tempStack = Stack()
    for i in range(amountToMove):
        item = stacks[columnToRemoveFrom].pop()
        tempStack.push(item)
    
    for i in range(amountToMove):
        item = tempStack.pop()
        stacks[columnToAddTo].push(item)

with open("input.txt", 'r') as f:
    #Allows for the counting of lines within the file
    lineCounter = 0
    for line in f:
        if(lineCounter > 9):
            #moveOneAtATime(line)
            moveMultiple(line)
        lineCounter += 1
        
for j in stacks:
    j.printStack()

