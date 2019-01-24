"""Linked List Components
-> We are given head, the head node of a linked list containing unique integer values.
-> We are also given the list G, a subset of the values in the linked list.
-> Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.
-> Example 1:
* Input:
* head: 0->1->2->3
* G = [0, 1, 3]
* Output: 2
* Explanation:
* 0 and 1 are connected, so [0, 1] and [3] are the two connected components.
-> Example 2:
* Input:
* head: 0->1->2->3->4
* G = [0, 3, 1, 4]
* Output: 2
* Explanation:
* 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
-> Note:
* If N is the length of the linked list given by head, 1 <= N <= 10000.
* The value of each node in the linked list will be in the range [0, N - 1].
* 1 <= G.length <= 10000.
* G is a subset of all values in the linked list.
** Approach:
#traverse through linked list, if element in linked list is in subset list given,
#check if next value is null and next value not equal to current value, increment count
#return count
# Time: O(n); Space - O(1)
"""
class LinkedListComponents(object):
    def __init__(self):
        self.head = None

    def countcomponent(self, head, lst):
        curr = head  # make curr as head
        count = 0  # default count is 0
        while curr:  # while curr, if curr data is in lst and (curr.next.data not in list and curr.next is null), increment count
            if(curr.data in lst and ((curr.next == None) or (curr.next.data not in lst))):
                count += 1
            curr = curr.next  # increment curr
        return count  # return count

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

list1 = LinkedListComponents()
list1.head = Node(0)
e2 = Node(1)
e3 = Node(2)
e4 = Node(3)
list1.head.next = e2
e2.next = e3
e3.next = e4
e4.next = None
print(list1.countcomponent(list1.head, [0, 1, 3]))

list2 = LinkedListComponents()
list2.head = Node(0)
e2 = Node(1)
e3 = Node(2)
e4 = Node(3)
e5 = Node(4)
list2.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = None
print(list2.countcomponent(list2.head, [0, 3, 1, 4]))
