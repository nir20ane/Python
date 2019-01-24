"""* Merge two sorted linked lists and return it as a new list.
 * The new list should be made by splicing together the nodes of the first two lists.
Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
*** Approach: Recusrion
* Time - O(n+m)
* Space - O(n+m), n+m stack frames are consumed
* """
class MergeTwoSortedListsRecursion(object):
    def __int__(self):
        self.head = None

    def mergelists(self, list1, list2):
        prehead = Node(-1)  # have a pre head as -1
        prev = prehead

        while list1 and list2:
            if list1.data < list2.data:  # if list1 val < list2 val, append list 1, increment list 1
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2  # if list2 val < list1 val, append list 2, increment list 2
                list2 = list2.next
            prev = prev.next

        if(list1 is None):
            prev.next = list2  # if list 1 is none append list 2

        if(list2 is None):
            prev.next = list1  # if list 2 is none append list 1
        print(prehead.next.data)
        return prehead.next  # return pre head next

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
