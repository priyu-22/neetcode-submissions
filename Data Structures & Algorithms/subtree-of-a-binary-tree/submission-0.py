# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare_dfs(node, subTreeNode):
            if not node and not subTreeNode:
                return True
            if node and subTreeNode and (node.val == subTreeNode.val):
                return (compare_dfs(node.left, subTreeNode.left) and compare_dfs(node.right, subTreeNode.right))
            return False
        if not subRoot:
            return True
        if not root:
            return False
        if compare_dfs(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        
        