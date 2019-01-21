"""Reverse a singly linked list - Iteration
Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
Use iteration, store next element, make element point to previous, update previous to element we are sitting on now,
update current to next
* time - O(n), space - O(1)
"""
class Node(object):
    def __init__(self, data=None):  # Node class creation
        self.data = data
        self.next = None  # class to create Nodes

class ReverseLinkedList_Iteration(object):
    def __init__(self):
        self.head = None  # have head as none

    def reversesll(self, head):  # pass head argument
        print(head.data)
        next = None
        prev = None
        curr = head
        while(curr != None):
            next = curr.next  # store next in temp
            curr.next = prev  # update next to point to prev
            prev = curr  # make prev as current
            curr = next  # make current as temp
        print(prev.data)
        return prev

rll = ReverseLinkedList_Iteration()
rll.head = Node(1)
n2 = Node(2)
rll.head.next = n2
n3 = Node(3)
n2.next = n3
rll.reversesll(rll.head)
