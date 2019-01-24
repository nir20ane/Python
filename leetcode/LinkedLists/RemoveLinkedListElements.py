"""Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.
Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
** Approach: first check with head, upadte curr to head and traverse using curr through the list
* Time - O(n); Space - O(1)
"""
class RemoveLinkedListElements(object):
    def __int__(self):
        self.head = None

    def remove(self, head, value):
        while head != None and head.val == value:  # check with head
            head = head.next  # move head
        current = head  # update curr
        while current != None and current.next != None:  # traverse through list using curr
            if current.next.val == value:
                current.next = current.next.next
            else:
                current = current.next
        return head

class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None

list1 = RemoveLinkedListElements()
list1.head = Node(6)
list1.head.next = Node(2)
list1.head.next.next = Node(6)
list1.head.next.next.next = Node(3)
list1.head.next.next.next.next = Node(4)
list1.head.next.next.next.next.next = Node(5)
list1.head.next.next.next.next.next = Node(6)
print(list1.remove(list1.head, 6).val)
