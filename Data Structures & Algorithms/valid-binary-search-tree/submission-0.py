# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # two conditions: 1. left side < root 2. right side > root
        # set two boundaries: left<node.val<right
        def dfs(left_boundary, node, right_boundary):
            if not node:
                return True
            if not (left_boundary < node.val and node.val < right_boundary):
                return False
            return (dfs(left_boundary, node.left, node.val) and
                dfs(node.val, node.right, right_boundary))
        return dfs(float("-inf"), root, float("inf"))