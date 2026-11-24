# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: i for i, val in enumerate(inorder)} # indexes for inorder array
        self.pre_i = 0 # indexes for preorder traversal
        def dfs(l, r):
            if l > r:
                return None
            root = TreeNode(preorder[self.pre_i])
            self.pre_i += 1
            mid = indices[root.val]
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root
        return dfs(0, len(inorder)-1)
