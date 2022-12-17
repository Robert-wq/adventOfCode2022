#Queue
#FIFO

#Functionality

#Add item to the back of the queue
#pop item from the front of the queue
#print queue
#check if queue is empty

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def isEmpty(self):
        return len(self.queue) <= 0
    
    def printQueue(self):
        for item in self.queue:
            print(item)
