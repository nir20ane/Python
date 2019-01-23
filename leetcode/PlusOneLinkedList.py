"""* Plus One Linked List
*Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.
*You may assume the integer do not contain any leading zero, except the number 0 itself.
*The digits are stored such that the most significant digit is at the head of the list.
*Example :
*Input: [1,2,3]
*Output: [1,2,4]
* Approach: keep track of last digit that is less than 9, add 1 to it, increment, then add zeroes till end
* Time : O(n); Space: O(1)
*/
"""
class PlusOneLinkedList(object):
    def __init__(self):
        self.head = None

    def addone(self, head):
        dummy = Node(0)  # create dummy node with 0 value
        i = dummy  # i and j to point to dummy
        j = dummy  # dummy to point head
        dummy.next = head
        while(j != None):
            if j.data < 9:
                i = j  # store last value less than 9 in 9
            j = j.next

        i.data = i.data + 1  # add 1 to i
        j = i.next  # increment i as make it as j
        while(j != None):
            j.data = 0  # add 0 until the end of list
            j = j.next

        if dummy.data == 0:
            return dummy.next  # if dummy.data == 0 return head

        return dummy  # else return dummy


class Node(object):
    def __init__(self, data=None):  # Node class creation
        self.data = data
        self.next = None

list1 = PlusOneLinkedList()
list1.head = Node(1)  # Node creation
e2 = Node(4)
e3 = Node(9)
e4 = Node(9)
list1.head.next = e2
e2.next = e3
e3.next = e4
n = list1.addone(list1.head)  # call addone method with list head
print(n.data)
print(n.next.data)
print(n.next.next.data)
print(n.next.next.next.data)
