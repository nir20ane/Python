"""Sort a linked list using insertion sort.
A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
Algorithm of Insertion Sort:
Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.
*** Time Complexity- O(n^2) - because of comparisons and swaps
*** Space Compleity - O(1)
"""
class InsertionSort(object):
    def __init__(self):
        self.head = None

    def sortlist(self, head):
        dummy = Node(0)
        prev = dummy
        curr = head
        while curr:
            prev = dummy
            while prev.next and prev.next.data < curr.data:  # move prev, when prev val is lower
                prev = prev.next
            next = curr.next  # swap logic
            curr.next = prev.next
            prev.next = curr
            curr = next
        return dummy.next

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

sortl = InsertionSort()
list1 = InsertionSort()
list1.head = Node(4)
e2 = Node(2)
e3 = Node(1)
e4 = Node(3)
list1.head.next = e2
e2.next = e3
e3.next = e4
e4.next = None

listnew = InsertionSort()
listnew = sortl.sortlist(list1.head)
while listnew:
    print listnew.data
    listnew = listnew.next
