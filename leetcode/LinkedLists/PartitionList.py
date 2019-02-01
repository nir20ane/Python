"""Partition List
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
** Approach: use before, before head, after, afterhead
* increment before and after based on node data
* join before.next and afterhead
* return before head
* Time complexity: O(N)
* Space Complexity: O(1)
"""

class PartitionList(object):
    def __init__(self):
        self.head = None

    def makepartition(self, head, x):
        beforehead = Node(0)
        before = beforehead
        afterhead = Node(0)
        after = afterhead
        while head:
            if head.data < x:  # is val < x, add to before
                before.next = head
                before = before.next
            else:
                after.next = head  # if val > x, add to after
                after = after.next
            head = head.next
        after.next = None
        before.next = afterhead.next  # join before and after
        return beforehead.next  # return beforehead.next

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

part = PartitionList()
list1 = PartitionList()
list1.head = Node(1)
e2 = Node(6)
e3 = Node(4)
e4 = Node(2)
e5 = Node(5)
e6 = Node(0)
list1.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
e6.next = None
partnew = part.makepartition(list1.head, 3)
while partnew is not None:
    print(partnew.data)
    partnew = partnew.next