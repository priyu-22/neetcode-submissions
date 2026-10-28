class Node:
    # Doubly linked list node.
    # Stores the KEY as well as the value: on eviction we find the LRU node in the
    # list and need its key to delete the matching hashmap entry in O(1).
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    # get and put are both O(1) average time; space is O(capacity).
    # Two data structures work together:
    #   1. hashmap  key -> node : find any key's node in O(1)
    #   2. doubly linked list   : order by recency, so we can move any node to the MRU
    #      end and evict from the LRU end in O(1).
    #      Must be DOUBLY linked: removing a node from the middle needs node.prev,
    #      which a singly linked list can't reach in O(1).
    # List layout (left -> right):
    #   [lru sentinel] <-> least recent ... most recent <-> [mru sentinel]

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # hashmap: key -> node

        # Two dummy (sentinel) nodes mark the ends of the list, so insert/remove
        # never need None checks, even when the cache is empty.
        # self.lru (left end): self.lru.next is always the least recently used node.
        # self.mru (right end): self.mru.prev is always the most recently used node.
        self.lru, self.mru = Node(0,0), Node(0,0)
        self.lru.next, self.mru.prev = self.mru, self.lru # empty list: lru <-> mru
        # DLL created with 2 dummy nodes

    # Helper 1: unlink a node from the doubly linked list.
    # Only touches the list; the hashmap entry is NOT removed here.
    def remove(self, node):
        # prev = neighbor on the LEFT (toward LRU), nxt = neighbor on the RIGHT (toward MRU).
        # Point the two neighbors at each other so the node drops out of the list.
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Helper 2: insert a node at the right end (MRU), just before the mru sentinel.
    def insert(self, node):
        # prev = current most recent node (or the lru sentinel if the list is empty)
        # nxt  = the mru sentinel
        prev = self.mru.prev
        nxt = self.mru
        prev.next = nxt.prev = node # chained assignment: both neighbors now point to node
        node.next = nxt
        node.prev = prev
    
    def get(self, key: int) -> int:
        # A successful get counts as a "use": move the node to the MRU end.
        if key in self.cache:
            # unlink the node from its current position
            self.remove(self.cache[key])
            # re-insert it at the MRU (right) end
            self.insert(self.cache[key])
            # return the node's value
            return self.cache[key].val

        return -1 # key not in cache

    def put(self, key: int, value: int) -> None:
        # If the key exists: unlink its old node (a fresh node replaces it below).
        # Then add the new node at the MRU end; if over capacity, evict from the LRU end.
        # NOTE: updating the existing node's val in place and moving it would avoid
        # allocating a new node; this version replaces the node instead.
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value) # create a new node and map key -> node
        self.insert(self.cache[key]) # add it at the MRU (right) end

        # Over capacity? Evict the least recently used node (lru.next).
        if len(self.cache) > self.cap:
            lru = self.lru.next
            self.remove(lru) # unlink from the list
            del self.cache[lru.key] # remove from the hashmap (this is why Node stores key)