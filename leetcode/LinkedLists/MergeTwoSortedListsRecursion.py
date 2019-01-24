"""* Merge two sorted linked lists and return it as a new list.
 * The new list should be made by splicing together the nodes of the first two lists.
Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
*** Approach: Recursion
* Time - O(n+m)
* Space - O(n+m), n+m stack frames are consumed
* """
class MergeTwoSortedListsRecursion(object):
    def __int__(self):
        self.head = None

    def mergelists(self, list1, list2):
        if list1 is None:
            return list2  # if list1 is none, return list2
        elif list2 is None:
            return list1  # if list2 is none, return list1
        elif list1.data < list2.data:
            list1.next = self.mergelists(list1.next, list2)  # if list1 val < list2 val, increment list1.next to merge result and return list1
            return list1
        else:
            list2.next = self.mergelists(list1, list2.next)  # if list2 val < list1 val, increment list2.next to merge result and return list2
            return list2

class Node(object):
    def __init__(self, data=None):  # Node class creation
        self.data = data
        self.next = None

list1 = MergeTwoSortedListsRecursion()  # List l1 creation
list1.head = Node(1)
e2 = Node(6)
e3 = Node(8)
list1.head.next = e2
e2.next = e3
e3.next = None

list2 = MergeTwoSortedListsRecursion()  # List l2 creation
list2.head = Node(2)
e2 = Node(3)
e3 = Node(4)
list2.head.next = e2
e2.next = e3
e3.next = None
list1.mergelists(list1.head, list2.head)
print(list1.head.next.data)
