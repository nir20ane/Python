"""Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
Note: Do not modify the linked list.
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

** Approach: have two pointers, when slow is fast it means slow has completed a whole cycle
*  have another pointer slow2 as head, move slow2 and slow, when they intersect we will get the node at which cycle started
*  Time Complexity: O(N^2)
*  Space Complexity: O(n)
*"""
class LinkedListCycleII(object):
    def __init__(self):
        self.head = None

    def cycleindex(self, head):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next  # fast and slow pointers for traversing
            if slow == fast:  # when fast and slow meet have a new pointer
                slow2 = head
                while slow2 != slow:  # when new pointer and slow meet we get index
                    slow = slow.next
                    slow2 = slow2.next
                return slow2
        return None

class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None

list1 = LinkedListCycleII()
list1.head = Node(3)
list1.head.next = Node(2)
list1.head.next.next = Node(0)
list1.head.next.next.next = Node(-4)
list1.head.next.next.next.next = list1.head.next
print(list1.cycleindex(list1.head).val)

list2 = LinkedListCycleII()
list2.head = Node(3)
list2.head.next = Node(2)
list2.head.next.next = Node(0)
list2.head.next.next.next = Node(-4)
list2.head.next.next.next.next = list2.head
print(list2.cycleindex(list2.head).val)
