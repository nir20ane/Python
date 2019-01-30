"""You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
*** Approach: Elementary addition
** Time Complexity: O(max(m,n))
** Space Complexity: O(max(m,n))
"""
class AddTwonNmberslc(object):
    def __init__(self):
        self.head = None

    def addtwonumberslc(self, head1, head2):
        dummy = Node(0)
        p = head1
        q = head2
        curr = dummy
        carry = 0
        while p != None or q != None:
            if p != None:
                x = p.data
            else:
                x = 0
            if q != None:
                y = q.data
            else:
                y = 0
            summ = x + y + carry  # add values - carry
            carry = summ//10
            curr.next = Node(summ % 10)  # create new node for sum
            curr = curr.next
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next  # increment p and q
        if carry > 0:
            curr.next = Node(carry)  # if carry > 0, create new node
        while(dummy.next != None):
            print dummy.next.data
            dummy.next = dummy.next.next
        return dummy.next  # return new list

class Node(object):
    def __init__(self, data = None):
        self.data = data
        self.next = None

add = AddTwonNmberslc()
list1 = AddTwonNmberslc()
list1.head = Node(8)
e2 = Node(7)
e3 = Node(8)
list1.head.next = e2
e2.next = e3
e3.next = None
list2 = AddTwonNmberslc()
list2.head = Node(4)
e2 = Node(7)
e3 = Node(9)
list2.head.next = e2
e2.next = e3
e3.next = None
add.addtwonumberslc(list1.head, list2.head)
