from collections import deque
import time

class Queue:
	def __init__(self):
		self.arr = deque()

	def enqueue(self,elt):
		self.arr.appendleft(elt)

	def dequeue(self):
		self.arr.pop()

	def getLen(self):
		print(len(self.arr))

	def display(self):
		print(self.arr)

	def getLast(self):
		return self.arr[-1]

	def place_order(self,orders):
		for i in range(len(orders)):
			self.enqueue(orders[i])
			time.sleep(0.5)

	def serve_order(self):
		for i in range(len(self.arr)):
			print(self.arr.pop())
			time.sleep(5)

def produced_binary(n):
	q = Queue()
	q.enqueue('1')

	for i in range(n):
		val = q.getLast()
		print(' ',val)
		q.enqueue(val + '0')
		q.enqueue(val + '1')

		q.display()
		q.dequeue()
produced_binary(10)
"""orders = ['pizza','samosa','pasta','biryani','burger']
q.place_order(orders)
time.sleep(1)
q.serve_order()"""



