"""*Three in One: Describe how you could use a single array to implement three stacks.
 * I have implemented three stacks of capacity 10 using four five methods
 * createlist() - created new stacknodes array
 * push(int stacknum, int value) - pushes value, checks for overflow, increments size, update top
 * pop(int stacknum, int index) - pops and returns Node, checks for underflow
 * greefreeindex() - gets current free index, updates index
 * freenode(int index) - deletes Node at a particular index decrements size
 *"""
from StackNode import StackNode

class StackFromArray(StackNode):
    def __init__(self):
        self.capacity = 10
        self.size = 0
        self.stackpointers = [-1, -1, -1]
        self.freelisttopindex = 0

        self.stacknodes = [StackNode]*(self.capacity+1)
        self.buildfreelist()

    def buildfreelist(self):
        for i in range(self.capacity+1):
            self.stacknodes[i] = StackNode(0, i+1)

    def stackpush(self, stacknum, value):
        currfreeindex = self.getfreenodeindex()
        currstcktop = self.stackpointers[stacknum - 1]
        curr = self.stacknodes[currfreeindex]
        curr.value = value
        curr.next = currstcktop
        self.stackpointers[stacknum - 1] = currfreeindex

    def stackpop(self, stacknum):
        currstcktop = self.stackpointers[stacknum - 1]
        if currstcktop == -1:
            raise Exception('Under flow')
        temp = self.stacknodes[currstcktop]
        self.stackpointers[stacknum - 1] = temp.next
        self.freenode(currstcktop)
        return temp

    def getfreenodeindex(self):
        temp = self.freelisttopindex
        if self.size >= self.capacity:
            raise Exception('OVER FLOW')
        self.freelisttopindex = self.stacknodes[temp].next
        self.size += 1
        return temp

    def freenode(self, index):
        self.stacknodes[index].next = self.freelisttopindex
        self.freelisttopindex = index
        self.size -= 1

stackfromarr = StackFromArray()
stackfromarr.stackpush(1, 3)
stackfromarr.stackpush(1, 4)
stackfromarr.stackpush(1, 5)
stackfromarr.stackpush(1, 6)
stackfromarr.stackpush(1, 7)
stackfromarr.stackpush(2, 8)
stackfromarr.stackpush(3, 9)
tempnode = stackfromarr.stackpop(3)
print tempnode.value
tempnode = stackfromarr.stackpop(1)
print tempnode.value
tempnode = stackfromarr.stackpop(1)
print tempnode.value
