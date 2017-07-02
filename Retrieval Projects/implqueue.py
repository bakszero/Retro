class Queue:
    def __init__(self):
        self.arr = []
    
    def enqueue(self, item):
        self.arr.insert(0,item)

    def dequeue(self):
        self.arr.pop()

    def isEmpty(self):
        return self.arr == []
    
    def size (self):
        return len(self.arr)

q = Queue()

q.enqueue(5)
q.enqueue(17)

print (q.arr)