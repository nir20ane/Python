"""Given a sorted linked list, delete all duplicates such that each element appear only once.
Example 1:
Input: 1->1->2
Output: 1->2
Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
** Approach: if val == next.val, then remove the next, else move to next val
"""
class RemoveDuplicatesfromSortedList(object):

    def __init__(self):
        self.head = None

    def removeduplicates(self, list):
        current = list
        while current != None and current.next != None:
            if current.val == current.next.val:
                current.next = current.next.next  # remove element
            else:
                current = current.next
        print(list.val)
        print(list.next.val)
        return list

class Node(object):
    def __init__(self, val = None):
        self.val = val
        self.next = None

list1 = RemoveDuplicatesfromSortedList()  # create list 1
list1.head = Node(1)
list1.head.next = Node(1)
list1.head.next.next = Node(2)
list1.head.next.next.next = None
list1.removeduplicates(list1.head)

list2 = RemoveDuplicatesfromSortedList()  # create list 2
list2.head = Node(1)
list2.head.next = Node(1)
list2.head.next.next = Node(2)
list2.head.next.next.next = Node(3)
list2.head.next.next.next.next = Node(3)
list2.removeduplicates(list2.head)
