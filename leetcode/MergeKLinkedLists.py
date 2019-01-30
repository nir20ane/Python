"""Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
** Approach: Use Priority Queue
** Time Complexity O(nlogk) k = is number of operations of PQ
** n is number of nodes in final list
** Space Complexity is O(n)
"""
from Queue import PriorityQueue

class MergeKLinkedLists(object):
    def __init__(self):
        self.head = None

    def mergelinkedlists(self, lists):
        head = curr = Node(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.data, l))  # insert every list in queue

        while not q.empty():
            data, node = q.get()   # traverse through queue, insert every node in every list
            curr.next = Node(data)
            curr = curr.next
            node = node.next
            if node:
                q.put((node.data, node))

        curr = head.next
        while curr:
            print curr.data
            curr = curr.next

        return head.next

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


merge = MergeKLinkedLists()
list1 = MergeKLinkedLists()
list1.head = Node(8)
e2 = Node(7)
e3 = Node(8)
list1.head.next = e2
e2.next = e3
e3.next = None

list2 = MergeKLinkedLists()
list2.head = Node(4)
e22 = Node(7)
e32 = Node(9)
list2.head.next = e22
e22.next = e32
e32.next = None

list3 = MergeKLinkedLists()
list3.head = Node(5)
e23 = Node(3)
e33 = Node(8)
list3.head.next = e23
e23.next = e33
e33.next = None
merge.mergelinkedlists([list1.head, list2.head, list3.head])
