"""Rotate List
Given a linked list, rotate the list to the right by k places, where k is non-negative.
Example 1:
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
** Approach:
Since k may be a large number compared to the length of list.
So we need to know the length of linked list.After that, move the list after the (l-k%l )th node to the front to finish the rotation.
Ex: {1,2,3} k=2 Move the list after the 1st node to the front
Ex: {1,2,3} k=5, In this case Move the list after (3-5%3=1)st node to the front.
So the code has three parts.
1.Get the length
2. Move to the (l-k%l)th node
3.Do the rotation
*** Time Complexity: O(N)
*** Space Complexity: O(1)
"""
class RotateList(object):
    def __init__(self):
        self.head = None

    def rotate(self, head, x):
        dummy = Node(0)
        fast = dummy
        slow = dummy
        dummy.next = head
        l = 0

        while fast.next != None:
            fast = fast.next  # Move fast till end and get length
            l += 1

        for j in range(l-x%l):
            slow = slow.next  # get new end of new rotate list

        fast.next = dummy.next
        dummy.next = slow.next  # join both and remove disconnect previous connection
        slow.next = None
        return dummy.next  # return new list

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

rot = RotateList()
list1 = RotateList()
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
rotnew = rot.rotate(list1.head, 2)
while rotnew is not None:
    print(rotnew.data)
    rotnew = rotnew.next
