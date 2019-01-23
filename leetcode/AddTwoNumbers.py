"""* Add Two Numbers II
* You are given two non-empty linked lists representing two non-negative integers.
* The most significant digit comes first and each of their nodes contain a single digit.
* Add the two numbers and return it as a linked list.
* You may assume the two numbers do not contain any leading zero, except the number 0 itself.
* Follow up:
* What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
* Example:
* Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
* Output: 7 -> 8 -> 0 -> 7
* """

class AddTwoNumbers(object):
    def __init__(self):
        self.head = None

    def calclength(self, lst):
        count = 0
        while lst:  # calculate and return number of nodes in linked list
            count += 1
            lst = lst.next
        return count

    def addtwonums(self, list1, list2):
        len1 = self.calclength(list1)  # obtain length of list1 and list2
        len2 = self.calclength(list2)

        dummy = Node(1)  # make sure that value is 1, so as to take care of first digit at the end

        if len1 > len2:  # call helper based on len1 and len2
            dummy.next = self.helper(list1, list2, len1 - len2)
        else:
            dummy.next = self.helper(list2, list1, len2 - len1)

        if (dummy.next.data > 9):  # take care of first digit
            dummy.next.data = dummy.next.data % 10
            return dummy
        return dummy.next

    def helper(self, n, m, offset):
        if n is None:
            return None  # if n is None, return None
        if offset == 0:
            result = Node(n.data+m.data)  # add result if no offset
            pos = self.helper(n.next, m.next, 0)  # pass to next element
        else:
            result = Node(n.data)  # create node with element of bigger list
            pos = self.helper(n.next, m, offset-1)  # call helper with just list1 incremented to next, list2 and offset -1

        if(pos and pos.data > 9):  # take care of carry here
            pos.data = pos.data % 10
            result.data += 1
        result.next = pos  # append pos to result
        return result  # return result

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

list1 = AddTwoNumbers()
list1.head = Node(7)
e2 = Node(2)
e3 = Node(4)
e4 = Node(3)
list1.head.next = e2
e2.next = e3
e3.next = e4
e4.next = None

list2 = AddTwoNumbers()
list2.head = Node(5)
e2 = Node(6)
e3 = Node(4)
list2.head.next = e2
e2.next = e3
e3.next = None

print(list1.addtwonums(list1.head, list2.head).next.data)



