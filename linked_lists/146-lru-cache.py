class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val

        # pointers to previous and next node
        self.prev = None
        self.next = None 

class LRUCache:
    """
    Hashmap + Doubly Tailed Linked List

    O(1) time for all operations
    O(n) space
    """

    def __init__(self, capacity: int):
        self.cache: dict[int, ListNode] = {}
        self.capacity = capacity

        # doubly tailed linked list as our nodes
        # initially the list is empty
        self.head = None # lru
        self.tail = None # mru

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # move node to most recently used
        self.move_to_end(key)
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        # if key already in cache
        if key in self.cache:
            # update value and move to most recently used
            self.move_to_end(key)
            self.cache[key].val = value
            return

        # pop lru once capacity is reached
        if len(self.cache) == self.capacity:
            self.cache.pop(self.head.key)
            self.pop_head()

        self.cache[key] = ListNode(key, value)
        self.insert_tail(self.cache[key])

    def move_to_end(self, key: int) -> None:
        node = self.cache[key]

        # if node is the mru, no need to move it
        # occurs when we are calling it on the last element
        # (in the case when only one element, exit here too)
        if node == self.tail:
            return

        # Gurantees >= 2 elements
        prv: ListNode | None = node.prev
        nxt: ListNode = node.next # since node is not the tail, nxt always exists

        if prv is None: # node has no previous element (it is the lru)
            # make next element the new lru
            self.head = nxt
            nxt.prev = None
        else:
            prv.next = nxt
            nxt.prev = prv

        # disconnect current node
        node.next = None
        node.prev = None

        # insert node at tail (making it the mru)
        self.insert_tail(node)

    def insert_tail(self, node: ListNode) -> None:
        # insert node at linked list tail
        # no elements in the linked list
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
            return

        # connect tail to node
        self.tail.next = node
        node.prev = self.tail

        self.tail = node

    def pop_head(self) -> ListNode:
        # pop the head, ie. the lru
        node = self.head

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            nxt = node.next

            # disconnect node and next node
            node.next = None
            nxt.prev = None

            # set new lru
            self.head = nxt

        return node

"""
Python's OrderedDict:
Standard library implementation of ordered dictionary
using same hashmap + doubly linked list approach

O(1) time for all operations
O(n) space
"""

from collections import OrderedDict

class LRUCache2:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # move key to most recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # if key already in cache
        if key in self.cache:
            # update value and move to most recently used
            self.cache.move_to_end(key)
            self.cache[key] = value
            return

        # insert new key
        # pop lru once capacity is reached
        if len(self.cache) == self.capacity:
            self.cache.popitem(last=False)

        self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)