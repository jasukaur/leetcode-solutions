from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        
        # Move the accessed key to the end by popping and re-inserting
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key, value):
        if key in self.cache:
            # If key exists, move it to the end by popping and re-inserting
            self.cache.pop(key)
        self.cache[key] = value
        
        # If the size exceeds capacity, remove the least recently used item
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
