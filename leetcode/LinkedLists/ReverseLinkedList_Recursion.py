"""Reverse a singly linked list - Recursion
Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
* Use Recursion, assume that the list is reverse after recursion and point to the element before
* time - O(n), space - O(n) - because of stack operations
"""
class Node(object):
    def __init__(self, data=None):  # Node class creation
        self.data = data
        self.next = None  # class to create Nodes

class ReverseLinkedList_Recursion(object):
    def __init__(self):
        self.head = None  # have head as none

    def reversesll(self, head):  # pass head argument
        if(head == None or head.next==None):
            return head
        nextnode = head.next
        p = self.reversesll(nextnode)  # recursive call
        nextnode.next = head
        head.next = None
        #print(p.data)
        return p

rll = ReverseLinkedList_Recursion()
rll.head = Node(1)
n2 = Node(2)
rll.head.next = n2
n3 = Node(3)
n2.next = n3
n4 = Node(6)
n3.next = n4
rll.reversesll(rll.head)
