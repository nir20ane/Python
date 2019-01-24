"""Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.
Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
Approach:
1. Copy all elements to an array and return middle of the array/ Time - O(n); Space O(n)
2. Two runner, one slow and one fast, when fast runner reaches end, slow will be in the middle, Time - O(n); Space O(1)
"""
class Node(object):
    def __init__(self, data=None):  # Node class creation
        self.data = data
        self.next = None

class MiddleLinkedList(object):  # Middle of Linked list class
    def __init__(self):
        self.head = None

    def middle(self, head):  # middle method
        fast = head  # two pointers fast and slow
        slow = head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        print(slow.data)
        return slow  # return slow pointer

list1 = MiddleLinkedList()
list1.head = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
list1.head.next = e2
e2.next = e3
e3.next = e4
list1.middle(list1.head)
