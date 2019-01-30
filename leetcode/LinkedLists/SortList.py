"""Sort a linked list in O(n log n) time using constant space complexity.
Example 1:
Input: 4->2->1->3
Output: 1->2->3->4
Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
** Approach: Merge Sort
* Time Complexity - O(nlogn)
* Space Complexity - O(logn) beacuse of recursions
"""
class SortList(object):
    def __init__(self):
        self.head = None

    def sortlist(self, head):

        if head is None or head.next is None:
            return head

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next  # determine middle

        prev.next = None
        l1 = self.sortlist(head)
        l2 = self.sortlist(slow)  # sort from head and middle repeatedly via recusrion

        return self.mergeList(l1, l2)  # merge lists


    def mergeList(self, l1, l2):

        curr = Node(0)  # merge lists via recusrion
        prev = curr

        while l1 and l2:
            if l1.data < l2.data:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        if l1 is None:
            prev.next = l2

        if l2 is None:
            prev.next = l1

        return curr.next


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

sortl = SortList()
list1 = SortList()
list1.head = Node(4)
e2 = Node(2)
e3 = Node(1)
e4 = Node(3)
list1.head.next = e2
e2.next = e3
e3.next = e4
e4.next = None

listnew = SortList()
listnew = sortl.sortlist(list1.head)
while listnew:
    print listnew.data
    listnew = listnew.next
