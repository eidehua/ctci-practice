# Todo: make linked list a module
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
	


list = LinkedList()
list.addNode(5)
list.addNode(4)
list.addNode(3)
list.addNode(5)
list.printList()


# given an unsorted linked list, remove the duplicates
# eg: 5->4->3->5 
# after remove dup: 5->4->3

# as we go through the list, keep track of numbers seen in a dictionary (hashtable)
# note if the data were chars, we could potentially just have an array

def removeDups(list):
	curr = list.head
	elements = {}
	# no special case for head element, can't have dups with only 1 element
	elements[curr.data] = True
	prev = curr	
	curr = curr.next
	
	while curr != None:
		key = curr.data
		if key in elements:
			prev.next = curr.next # removes curr
		else:
			elements[key] = True
			prev = curr # only update prev if curr still exists as part of the linked list!
		curr = curr.next

removeDups(list)
list.printList()
# follow up: how would you solve this problem if a temporary buffer is not allowed
