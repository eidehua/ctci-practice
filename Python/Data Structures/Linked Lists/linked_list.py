class LinkedList:
	def __init__(self):
		self.head = None

	def addNode(self, data):
		if self.head == None:
			self.head = Node(data, None)
		else:
			curr = self.head
			while curr.next != None: # stops us on last node
				curr = curr.next
			curr.next = Node(data, None)
			
	def printList(self):
		curr = self.head
		while curr != None:
			print curr.data , # comma makes new line not happen
			curr = curr.next
		print
		

class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next
	