"""Linked List Cycle
Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.
approach: fast and slow runners
Time: O(N); Space: O(1)
"""
class LinkedListCycle(object):
    def __init__(self):
        self.head = None

    def cycledetect(self, head):
        if head is None or head.next is None:
            return False
        slow = head  # have fast and slow runners
        fast = head.next
        while slow is not fast:  # when slow is not fast and fast, fats.next is None return False
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next  # increment slow and fast
        return True  # return True

class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None


list1 = LinkedListCycle()
list1.head = Node(3)
list1.head.next = Node(2)
list1.head.next.next = Node(0)
list1.head.next.next.next = Node(-4)
list1.head.next.next.next.next = list1.head.next
print(list1.cycledetect(list1.head))

list2 = LinkedListCycle()
list2.head = Node(3)
list2.head.next = Node(2)
list2.head.next.next = Node(0)
list2.head.next.next.next = Node(-4)
list2.head.next.next.next.next = None
print(list2.cycledetect(list2.head))
