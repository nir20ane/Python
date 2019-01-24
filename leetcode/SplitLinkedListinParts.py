"""** Split Linked List in Parts
* Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".
* The length of each part should be as equal as possible: no two parts should have a size differing by more than 1.
* This may lead to some parts being null.
* The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.
* Return a List of ListNode's representing the linked list parts that are formed.
* Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
* * Example 1:
Input:
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
* Explanation:
* The input and each element of the output are ListNodes, not arrays.
* For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
* The first element output[0] has output[0].val = 1, output[0].next = null.
* The last element output[4] is null, but it's string representation as a ListNode is [].
* * Example 2:
Input:
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
* Explanation:
* The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
* Note:
* The length of root will be in the range [0, 1000].
* Each value of a node in the input will be an integer in the range [0, 999].
* k will be an integer in the range [1, 50].
* Time complexity = O(N+k)
* Space complexity = O(k)
*"""
class SplitLinkedListinParts(object):
    def __init__(self):
        self.head = None

    def split(self, root, k):
        curr = root
        length = 0
        while curr:
            length += 1
            curr = curr.next  # calculate length
        curr = root
        width = length//k
        remain = length % k  # calc width and remaining
        splits = []
        for i in range(k):
            head = curr
            if i < remain:
                val = width + 1 - 1  # calculate val based on width
            else:
                val = width + 0 - 1
            for j in range(val):
                if curr is not None:
                    curr = curr.next  # iterate curr
            if curr is not None:
                prev = curr  # make prev point to curr, increment curr
                curr = curr.next  # This is needed as head will now point to prev and the nodes following it
                prev.next = None
            splits.append(head)  # incremented curr will become new head in next i iteration
        return splits

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

list1 = SplitLinkedListinParts()
list1.head = Node(0)
e2 = Node(1)
e3 = Node(2)
e4 = Node(3)
list1.head.next = e2
e2.next = e3
e4.next = None
split = list1.split(list1.head, 2)
for s in split:
    print(s.data)
