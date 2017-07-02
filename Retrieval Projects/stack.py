class Stack:
	def __init__(self):
		self.arr=[]
	def isEmpty(self):
		return self.arr == []
	def push(self, item):
		return self.arr.append(item)
	def pop(self):
		return self.arr.pop()
	def size(self):
		return len(self.arr)
	def peek(self):
		return self.arr[len(self.arr)-1]


s = Stack()
s.push(3)
s.push(4)
print(s.peek())
s.pop()

