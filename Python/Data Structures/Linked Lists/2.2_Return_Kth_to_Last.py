from linked_list import LinkedList

# find kth to last element of a singly linked list
# Second to last = 2nd to last 
# 1st to last = last

list = LinkedList()
list.addNode(1)
list.addNode(2)
list.addNode(3)
list.addNode(4)
list.addNode(5)
list.addNode(6)
list.printList()

# we can run through the linked list to grab the size, N.
# Linked list elements are indexed 0, 1, ... N-1
# kth to last element. 
# 1st to last element = last element. = N - 1
# 2nd to last element = N - 2
# Nth to last element = N - N = 0 = first element

def get_kth_to_last(list, k):
	curr = list.head
	num_elements = 0
	while curr != None:
		curr = curr.next
		num_elements+=1
	index_we_want = num_elements - k
	if index_we_want < 0:
		return None
	curr = list.head # rewind iterator
	# say index we want is 1. We start at 0 (head), then move to element at 1. Then we should exit for loop
	for index in range(0, index_we_want): 
		curr = curr.next
	return curr.data
		

print get_kth_to_last(list, 2)
assert get_kth_to_last(list, 2) == 5
assert get_kth_to_last(list, 1) == 6

# Given a list of size N, this solution has a runtime of O(N)
# Space complexity: O(1)

# recursive
# iterative