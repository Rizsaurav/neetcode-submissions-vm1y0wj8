class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity =capacity

        #key -> node
        self.cache = {}
        #dummy head and tail so we never deal with empty list edge cases
        self.left = Node(0,0) #LRU end(least recent)
        self.right = Node(0,0) #MRU end (most recent)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self,node): #always insert at MRU end(right) 
        prev,nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev    

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) #remove from current position
            self.insert(self.cache[key]) #reinsert at. MRU end
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) #remove old node
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key]) #insert at MRU end

        if len(self.cache) > self.capacity:
            lru = self.left.next #LRU is just after left dummy
            self.remove(lru)
            del self.cache[lru.key]
        
