class Node:
    def __init__(self,key=0,value=0):
        self.key = key
        self.value = value
        prev = None
        next = None
class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {} # key -> key, value -> doubly LL address
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    def remove_node(self,node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    def add_node(self,node):
        end = self.tail.prev
        end.next = node
        node.prev = end
        node.next = self.tail
        self.tail.prev = node


    def get(self,key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_node(node)
        self.add_node(node)
        return node.value
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove_node(node)
            self.add_node(node)
        else:
            node = Node(key,value)
            self.cache[key] = node
            self.add_node(node)
            if len(self.cache) > self.capacity:
                lru_node = self.head.next
                self.remove_node(lru_node)
                del self.cache[lru_node.key]


