"""Given a singly linked list L: L0->L1->...->Ln->1->Ln,
reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2
You may not modify the values in the list's nodes, only nodes itself may be changed.
Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
** Approach: Split list into two, find Middle, reverse second half, and merge 1st and 2nd halves
* Time Complexity: O(n)
* Space Complexity : O(1)
*/
"""
class ReOrderList(object):
    def __init__(self):
        self.head = None

    def reorder(self, head):
        if head is None or head.next is None:
            return
        l1 = head
        fast = head
        slow = head
        prev = None
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None  # Split list into two halves

        l2 = self.reverse(slow)  # Reverse second half

        self.merge(l1, l2)  # Merge two lists

    def merge(self, l1, l2):
        while l1 is not None:
            n1 = l1.next
            n2 = l2.next
            l1.next = l2
            if n1 is None:
                break
            l2.next = n1
            l1 = n1
            l2 = n2

    def reverse(self, head):
        prev = None
        curr = head
        next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

reord = ReOrderList()
list1 = ReOrderList()
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
reord.reorder(list1.head)
while list1.head is not None:
    print(list1.head.data)
    list1.head = list1.head.next
