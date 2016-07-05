from linked_list import LinkedList
# import linked_list will get all top level functionality, then you gotta do linked_list.LinkedList
import linked_list
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
