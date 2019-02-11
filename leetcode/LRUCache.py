"""*LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?
Example:
LRUCache cache = new LRUCache( 2 capacity  );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
*"""
class LRUCache(object):
    def __init__(self, capacity=None):
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.map = {}
        self.head.next = self.tail
        self.tail.prev = self.head


    def put(self, key, value):
        if key in self.map:
            del self.map[key]
        if len(self.map) == self.capacity:
            self.remove(self.tail.prev)  # remove lst element if capacity is exceeded
        self.insert(Node(key, value))  # insert Node at head

    def get(self, key):
        if key in self.map:
            n = self.map[key]  # get and return node value if key node is present
            self.remove(n)
            self.insert(n)
            return n.value
        else:
            return -1  # else return -1


    def insert(self, node):
        self.map[node.key] = node  # insert in map as well as linked list
        acthead = self.head.next
        self.head.next = node
        node.next = acthead
        acthead.prev = node
        node.prev = self.head


    def remove(self, node):
        del self.map[node.key]  # remove from map as well as from linked list
        node.prev.next = node.next
        node.next.prev = node.prev

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
