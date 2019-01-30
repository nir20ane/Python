"""Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
** Approach: have odd, oddhead, even, even head
Time Complexity: O(n)
Space Compelxity: O(1) - no extra space is used
"""
class OddEvenLinkedList(object):
    def __init__(self):
        self.head = None

    def oddevenlist(self, head):
        odd = head
        even = head.next  # have even and even head
        evenh = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenh  # in the end make odd.next as even head
        return head

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

sortl = OddEvenLinkedList()
list1 = OddEvenLinkedList()
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

listnew = OddEvenLinkedList()
listnew = sortl.oddevenlist(list1.head)
while listnew:
    print listnew.data
    listnew = listnew.next