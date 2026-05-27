"""
list addition and removal of a node is O(n). That is costly. We can
optimize this using a doubly linked list
"""

class Node:
    def __init__(self,key=None,value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_node(self,node):
        last_node = self.tail.prev
        last_node.next = node
        node.prev = last_node
        node.next = self.tail
        self.tail.prev = node
    def remove_node(self,node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    def get(self,key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_node(node)
        self.add_node(node)
        return node.value
    def put(self,key,value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove_node(node)
            self.add_node(node)
        else:
            node = Node(key,value)
            self.add_node(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                lru_node = self.head.next
                del self.cache[lru_node.key]
                self.remove_node(lru_node)
            
    
        