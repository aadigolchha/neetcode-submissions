# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        low = -float('inf')
        high = float('inf')
        
        return self.dfs(low, high, root)
        
    def dfs(self, low, high, root):
        
        if not root:
            return True
        
        if root.val <= low or root.val >= high:
            return False

        left = self.dfs(low, root.val, root.left)
        right = self.dfs(root.val, high, root.right)

        return (left and right)
        
        

        
        