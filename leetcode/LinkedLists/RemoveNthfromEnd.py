"""Remove Nth Node From End of List
Given a linked list, remove the n-th node from the end of list and return its head.
Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Follow up:
Could you do this in one pass?
** Approach: one pass, first till n, then move first and second till end,
* that way difference between first and second is always n
* time complexity: O(n)
* space complexity: O(1)
"""
class RemoveNthfromEnd(object):
    def __init__(self):
        self.head = None

    def removenth(self, head, n):
        dummy = Node(0)
        dummy.next = head
        first = dummy
        second = dummy  # first and second pointers to dummy node

        i = 0
        while i <= n:
            first = first.next  # increment first till n
            i += 1
        while first:
            first = first.next  # till end, increment first and second
            second = second.next

        second.next = second.next.next  # remove nth node
        return dummy.next


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

sortl = RemoveNthfromEnd()
list1 = RemoveNthfromEnd()
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

listnew = RemoveNthfromEnd()
listnew = sortl.removenth(list1.head, 5)
while listnew:
    print listnew.data
    listnew = listnew.next
    