class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0,0) # default values
        self.left.next, self.right.prev = self.right, self.left
        
    def insert(self, node): # insert on the right side
        """This function puts the node in the list"""
        prev, nxt =  self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        
    def remove(self, node): # remove on the left side
        """This function removes the node from the list"""
        prev, nxt = node.prev , node.next
        prev.next, nxt.prev = nxt, prev
        
    def get(self, key: int) -> int: 
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lr = self.left.next
            self.remove(lr)
            del self.cache[lr.key]
