"""
brute force solution -> Need something to track order. How does LRU
know when to pop? Have array/list that keeps track of every value, if value
is updated, pop list[key] and append it at the end. O(n) every time
"""

class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []
    
    def get(self,key):
        if key not in self.cache:
            return -1
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]
    def put(self,key,value):
        if key in self.cache:
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                lru_key = self.order.pop(0)
                del self.cache[lru_key]
            self.order.append(key)