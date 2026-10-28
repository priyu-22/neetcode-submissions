class Node:
    # Node class to create doubly linked list to track MRU and LRU
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    # all operations tc: O(1). remove least recently used
    #two data structures used: hashmap and Doubly linked list
    # track MRU (head or right-side) and LRU (tail or left-side)

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # a hashmap which maps key -> node

        # create a doubly linked list
        self.lru, self.mru = Node(0,0), Node(0,0)
        self.lru.next, self.mru.prev = self.mru, self.lru #lru next -> mru and mru pre -> lru doubly LL pointers defined
        # DLL created with 2 dummy nodes

    # helper function 1: remove node from hashmap and doubly LL
    def remove(self, node):
        # unlink the node from list. 
        prev, nxt = node.prev, node.next #prev is mru/right-side node and nxt is lru/left-side node
        prev.next, nxt.prev = nxt, prev

    # helper function 2: insert node next to mru/right side
    def insert(self, node):
        #insert node in right side/mru
        prev = self.mru.prev
        nxt = self.mru
        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev
    
    def get(self, key: int) -> int:
        # move this node to right - MRU
        #if key is in cache map
        if key in self.cache:
            # remove its node from list
            self.remove(self.cache[key])
            # inset it near mru(right side)
            self.insert(self.cache[key])
            # return the node's value
            return self.cache[key].val

        return -1 #if key is not in cache map return -1

    def put(self, key: int, value: int) -> None:
        # if already exists - move to right/MRU
        # else remove LRU and put existing MRU to LRU and add new node to MRU
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value) # create new node for new put value and add it to cache map
        self.insert(self.cache[key]) #insert it into doubly LL

        # track the len of cache map if it exceeds the given capacity
        if len(self.cache) > self.cap:
            lru = self.lru.next
            self.remove(lru) # remove left side node
            del self.cache[lru.key] # delete from cache map
