"""
hashmap = {key: doubly linked list}

"""
import threading

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.hash = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        self.lock = threading.Lock()

    def add(self, node): # L <-> A <-> B <-> R
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next

    def remove(self, node): # L <-> A <-> B <-> R
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def get(self, key: int) -> int:
        with self.lock:
            if key in self.hash:
                self.remove(self.hash[key])
                self.add(self.hash[key])
                return self.hash[key].val

            return -1        

    def put(self, key: int, value: int) -> None:
        with self.lock:
            if key in self.hash:
                self.remove(self.hash[key])
            self.hash[key] = Node(key, value)
            self.add(self.hash[key])

            # remove if we exceed capacity
            if len(self.hash) > self.cap:
                lru = self.left.next
                self.remove(lru)
                del self.hash[lru.key]
