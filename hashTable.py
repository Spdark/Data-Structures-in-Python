class Hashtable:
	def __init__(self):
		self.MAX = 100
		self.arr = [[] for i in range(self.MAX)]

	def get_hash(self,key):
		hash = 0
		for char in key:
			hash += ord(char)
		return hash%self.MAX

	def __setitem__(self,key,val):
		h = self.get_hash(key)
		self.arr[h] = val

	def __getitem__(self,index):
		h = self.get_hash(index)
		return self.arr[h]

	def __delitem__(self,key):
		h = self.get_hash(key)
		self.arr[h] = None

t = Hashtable()
t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 110
t["march 9"] = 460
t["march 10"] = 370
t["march 11"] = 440
print(t["march 11"])