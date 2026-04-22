from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    #Enqueue Add element to rear
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} added to queue")

    # Safe Dequeue Remove element from rear
    def safe_dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty, cannot dequeue")
            return None
        else:
            return self.queue.popleft()
        
    # Display Queue 
    def display(self):
        print("Queue: ", list(self.queue))

My_Queue = Queue()

My_Queue.enqueue(10)
My_Queue.enqueue(20)
My_Queue.enqueue(30)

print("Dequeued: ", My_Queue.safe_dequeue())
print("Dequeued: ", My_Queue.safe_dequeue())
print("Dequeued: ", My_Queue.safe_dequeue())

# Trying to dequeue from empty queue
print("Dequeued: ", My_Queue.safe_dequeue())