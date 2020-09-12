class BST:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def add_child(self,data):
		if self.data == data:
			return

		if self.data > data:
			if(self.left):
				self.left.add_child(data)
			else:
				self.left = BST(data)
		else:
			if(self.right):
				self.right.add_child(data)
			else:
				self.right = BST(data)

	def search(self,val):
		if self.data == val:
			return True

		if self.data > val:
			if self.left:
				return self.left.search(val)
			else:
				return False
		else:
			if self.right:
				return self.right.search(val)
			else:
				return False
	def in_order_traversal(self):
		elts = []
		if self.left:
			elts += self.left.in_order_traversal()

		elts.append(self.data)
		if self.right:
			elts += self.right.in_order_traversal()

		return elts

	def pre_order_traversal(self):
		elts = [self.data]
		if self.left:
			elts += self.left.in_order_traversal()

		if self.right:
			elts += self.right.in_order_traversal()

		return elts

	def post_order_traversal(self):
		elts = []

		if self.left:
			elts += self.left.in_order_traversal()

		if self.right:
			elts += self.right.in_order_traversal()

		elts.append(self.data)

		return elts

	def delete(self,val):
		if val > self.data:
			return self.right.delete(val)
		elif val < self.data:
			return self.left.delete(val)
		else:
			if self.left is None and self.right is None:
				return None
			elif self.left is None:
				return self.right
			elif self.right is None:
				return self.left

			min_val = self.right.find_min()
			self.data = min_val
			self.right = self.right.delete(min_val)

		return self

	def find_min(self):
		if self.left is None:
			return self.data
		return self.left.find_min()

	def find_max(self):
		if self.right is None:
			return self.data
		return self.right.find_max()

	def calculatesum(self):
		left_sum = self.left.calculatesum() if self.left else 0
		right_sum = self.right.calculatesum() if self.right else 0
		return self.data + left_sum + right_sum

def build_tree(arr):
	root = BST(arr[0])
	for i in range(1,len(arr)):
		root.add_child(arr[i])

	return root

if __name__ == '__main__':
	countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
	country_tree = build_tree(countries)
			
	print(country_tree.search("UK"))
	print(country_tree.search("Sweden"))

	numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
	print(numbers_tree.in_order_traversal())
	print(numbers_tree.pre_order_traversal())
	print(numbers_tree.post_order_traversal())

	numbers_tree.delete(20)
	print(numbers_tree.in_order_traversal())

	print(numbers_tree.calculatesum())