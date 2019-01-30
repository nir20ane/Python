"""Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.
Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:
Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
** Approach: Swap two nodes and move pointers ahead
* Time Complexity: O(N)
* Space Complexity: O(1)
"""
class SwapNodesinPairs(object):
    def __init__(self):
        self.head = None

    def swappairs(self, head):
        dummy = Node(0)
        prev = dummy
        dummy.next = head  # assume a dummy head

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next  # swap first nodes at a time
            first.next = second.next
            prev.next = second
            prev.next.next = first
            prev = prev.next.next  # skip two nodes

        return dummy.next

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

sortl = SwapNodesinPairs()
list1 = SwapNodesinPairs()
list1.head = Node(0)
e2 = Node(1)
e3 = Node(2)
e4 = Node(3)
e5 = Node(4)
e6 = Node(5)
list1.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
e6.next = None

listnew = SwapNodesinPairs()
listnew = sortl.swappairs(list1.head)
while listnew:
    print listnew.data
    listnew = listnew.next
