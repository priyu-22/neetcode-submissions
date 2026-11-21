# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        #helper function: we use depth to indicate the tree level
        def dfs(node, depth):
            if not node:
                return None
            if depth == len(res): # res array will have exactly 1 element for each level
                res.append(node.val)
            dfs(node.right, depth+1) #imp: call dfs on right side before left side
            dfs(node.left, depth+1)
        dfs(root, 0)
        return res
