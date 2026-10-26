"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Two pass + hashmap
        oldToCopy = {None:None} # EDGE CASE: if any pointer is pointing to null node the we want to map it to None node
        #FIRST PASS: create copy nodes of old nodes and update it in hashmap
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        # SECOND PASS: copy/update the pointers
        cur = head
        while cur:
            copyNode = oldToCopy[cur] #get copy from the hasmap
            copyNode.next = oldToCopy[cur.next]
            copyNode.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]