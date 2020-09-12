class Stack:
	def __init__(self):
		self.arr = []

	def push(self,elt):
		self.arr.append(elt)

	def pop(self):
		self.arr.pop()

	def getLen(self):
		print("Length of the Stack ",len(self.arr))

	def display(self):
		for i in self.arr:
			print("Elts ",i)

	def string_reverse(self,string):
		rev = ''
		for i in range(len(string)):
			self.arr.append(string[i])
		while(len(self.arr) != 0):
			temp = self.arr.pop()
			rev = rev + temp
		print(rev)

	def is_balanced(self,string):#({a+b})
		if string[0] == '}' or string[0] == ']' or string[0] == ')':
			return False
		for i in range(len(string)):
			if string[i] == '{' or string[i] == '[' or string[i] == '(':		
				self.arr.append(string[i])
			if string[i] == '}':
				if self.arr[len(self.arr)-1] == '{':
					self.arr.pop()
			if string[i] == ']':
				if self.arr[len(self.arr)-1] == '[':
					self.arr.pop()
			if string[i] == ')':
				if self.arr[len(self.arr)-1] == '(':
					self.arr.pop()
		if len(self.arr) == 0:
			return True
		return False

s = Stack()
string = '[a+b]*(x+2y)*{gg+kk}'
print(s.is_balanced(string))