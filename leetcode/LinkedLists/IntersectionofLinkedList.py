"""* Intersection of Two Linked Lists
Write a program to find the node at which the intersection of two singly linked lists begins.
** Approach: get the length of lists, adjust length to be equal, compare to find intersection
* Time O(n); Space O(1)
* """
class IntersectionofLinkedList(object):
    def __init__(self):
        self.head = None

    def intersect(self, head1, head2):
        len1 = self.length(head1)
        len2 = self.length(head2)  # length of list1 and list2

        while len1 > len2:
            head1 = head1.next  # adjust length of list1
            len1 -= 1

        while len2 > len1:
            head2 = head2.next  # adjust length of list 2
            len2 -= 1

        while head1 != head2:
            head1 = head1.next  # increment if nodes are not equal
            head2 = head2.next

        print(head1.data)
        return head1  # return node

    def length(self, curr):
        count = 0
        while curr != None:
            count += 1
            curr = curr.next
        return count

class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.next = None

list1 = IntersectionofLinkedList()  # create list 1
list1.head = Node(4)
list1.head.next = Node(1)
list1.head.next.next = Node(8)
list1.head.next.next.next = Node(4)
list1.head.next.next.next.next = Node(5)

list2 = IntersectionofLinkedList()  # create list 2
list2.head = Node(5)
list2.head.next = Node(1)
list2.head.next.next = Node(0)
list2.head.next.next.next = list1.head.next.next
list1.intersect(list1.head, list2.head)
