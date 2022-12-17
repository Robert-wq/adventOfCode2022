from Queue import *

queue = Queue()

print(queue.isEmpty())

for i in range(0, 10):
    queue.enqueue(i)

queue.printQueue()
print(queue.isEmpty())

q1 = queue.dequeue()
q2 = queue.dequeue()
q3 = queue.dequeue()

queue.printQueue()

print(q1)
print(q2)
print(q3)

