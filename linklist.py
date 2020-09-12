class Node:
	def __init__(self,data = None,next= None):
		self.data = data
		self.next = next

class Linklist:
	def __init__(self):
		self.head = None

	def printt(self):
		if self.head is None:
			print("Linklist is Empty")

		itr = self.head
		lis = ''
		while itr:
			lis += str(itr.data) + '-->'
			itr = itr.next
		print(lis)

	def getlen(self):
		itr = self.head
		c = 0
		while itr:
			c += 1
			itr = itr.next
		return c

	def insert_at_beg(self,data):
		node = Node(data,self.head)
		self.head = node

	def insert_at_end(self,data):
		if self.head is None:
			self.head = Node(data,self.head)
			return

		itr = self.head
		while itr.next:
			itr = itr.next
		itr.next = Node(data,None)

	def insert_at(self,pos,data):
		if pos == 1:
			self.insert_at_beg(data)
		if self.getlen() == pos:
			self.insert_at_end(data)
		c = 1
		p = self.head
		while p:
			if(c == pos):
				p.next = Node(data,p.next)
				break
			c += 1
			p = p.next

	def remove_at(self,pos):
		if(pos == 0):
			self.head = self.head.next
		p = self.head
		c = 0
		while p:
			if(c == pos-1):
				p.next = p.next.next
				break
			p = p.next
			c += 1

	def insert_after_value(self, data_after, data_to_insert):
		p = self.head
		while p:
			if(p.data == data_after):
				p.next = Node(data_to_insert,p.next)
			p = p.next

	def remove_by_value(self, data):
		p = self.head
		while p:
			if(p.next.data == data):
				p.next = p.next.next
				break
			p = p.next

ll = Linklist()

ll.insert_at_beg(1)
ll.insert_at_beg(2)
ll.insert_at_beg(3)
ll.insert_at_beg(4)

ll.insert_after_value(1,56)

ll.printt()
ll.remove_by_value(3)
ll.printt()