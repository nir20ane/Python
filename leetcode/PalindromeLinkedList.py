"""Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.
Example 1:
Input: 1->2
Output: false
Example 2:
Input: 1->2->2->1
Output: true
** Approach: get middle of list, and then reverse one half, then compare the nodes
* Time - O(n); Space - O(1)
"""
class PalindromeLinkedList(object):
    def __init__(self):
        self.head = None

    def palindrome(self, head):
        fast = head
        slow = head
        while fast != None and fast.next != None:  # fast and slow runners
            fast = fast.next.next
            slow = slow.next

        if fast!= None:  # if length is odd, adjust slow
            slow = slow.next

        slow = self.reverse(slow)  # reverse slow
        fast = head  # make fast as head

        while slow != None:  # compare nodes and increment fast and slow
            if fast.data != slow.data:
                return False
            fast = fast.next
            slow = slow.next
        return True

    def reverse(self, head):  # reverse method to reverse list
        next = None
        current = head
        prev = None
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

pll = PalindromeLinkedList()
pll.head = Node(1)
n2 = Node(2)
n3 = Node(2)
n4 = Node(1)
pll.head.next = n2
pll.head.next.next = n3
pll.head.next.next.next = n4
pll.head.next.next.next.next = None
print(pll.palindrome(pll.head))
