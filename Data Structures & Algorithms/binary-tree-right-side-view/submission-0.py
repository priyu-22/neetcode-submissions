# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root]) #initialize queue with root node list [[root]]
        while q:
            # get right most element
            rNode = None # every level rNode is initialized with none
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    print(node.val)
                    rNode = node #rNode gets overridden in every iteration of for loop. Hence in the end of the loop rNode will be rightmost element at each level
                    q.append(node.left)
                    q.append(node.right)
            if rNode:
                res.append(rNode.val)
        return res
