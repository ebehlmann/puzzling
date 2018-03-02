"""
You have a linked list and want to find the kkth to last node.
Write a function kth_to_last_node() that takes an integer kk and the head_node of a singly-linked list, and returns the kkth to last node in the list.
"""

class LinkedListNode:

    def __init__(self, value):
        self.value    = value
        self.next     = None
        self.previous = None

# get the length of the list
def find_list_size(head_node):
	i = head_node
	size = 0
	while i:
		i = i.next
		size += 1
	return size

# find kth-to-last node for linked list that starts with head_node
def kth_to_last_node(kk, head_node):
	list_size = find_list_size(head_node)
	steps_to_travel = list_size - kk
	i = head_node
	while steps_to_travel > 0:
		i = i.next
		steps_to_travel -= 1
	return i.value

# run with given example. Expected result: Devil's Food
a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

print(kth_to_last_node(2, a))