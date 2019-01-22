"""Write a function to delete a node (except the tail) in a singly linked list,
 * given only access to that node.
 * Given linked list -- head = [4,5,1,9], which looks like following:
 *
 * """
class DeletefromList(object):
    def __init__(self):
        self.head = Node

    def delete(self, list1):
        if(list1.next is not None):  # delete node is node is not tail
            list1.data = list1.next.data
            print(list1.data)
            list1.next = list1.next.next

class Node(object):
    def __init__(self, data = None):
        self.data = data
        self.next = None

list1 = DeletefromList();
list1.head = Node(1)
list1.head.next = Node(2)
list1.head.next.next = Node(3)
list1.head.next.next.next = Node(4)
list1.head.next.next.next.next = Node(5)
list1.delete(list1.head.next.next)