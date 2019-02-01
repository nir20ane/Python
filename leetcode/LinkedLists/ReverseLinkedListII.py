""""*Reverse Linked List II
Share
Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 < m < n < length of list.
Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
* Approach:
* till m, increment pointer
* till n-m; do reverse, with tail = prev.next
* Time Complexity : O(N)
* Space Complexity: O(1)
*/ """

class ReverseLinkedListII(object):
    def __init__(self):
        self.head = None

    def reversebetween(self, head, m, n):
        if head is None or head.next is None:
            return None
        dummy = Node(0)
        prev = dummy
        dummy.next = head
        for i in range(m-1):
            prev = prev.next  # till m, keep incrementing pointer

        tail = prev.next  # make tail as prev.next

        for j in range(n-m):  # till n-m, do reverse using prev and tail
            temp = prev.next
            prev.next = tail.next
            tail.next = tail.next.next
            prev.next.next = temp
        return dummy.next

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

rev = ReverseLinkedListII()
list1 = ReverseLinkedListII()
list1.head = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)
list1.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = None
newrev = rev.reversebetween(list1.head, 2, 4)
while newrev is not None:
    print(newrev.data)
    newrev = newrev.next
