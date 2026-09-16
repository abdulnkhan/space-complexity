class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # {key1: Node1, key2: Node2}

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node): #insert on right most side
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next
        

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    
    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache.keys()) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
