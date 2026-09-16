# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def getHeight(node):
            if not node:
                return 0
            height_of_left = getHeight(node.left)
            height_of_right = getHeight(node.right)
            return 1 + max(height_of_left, height_of_right)
        left_height = getHeight(root.left)
        right_height = getHeight(root.right)
        is_balanced = abs(left_height-right_height) <= 1
        if not is_balanced:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)