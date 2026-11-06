# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good = []

        def dfs(root, limit):

            nonlocal good

            if not root:
                return
            
            if root.val >= limit:
                good.append(root.val)
                limit = root.val

            
            dfs(root.left, limit)
            dfs(root.right, limit)

        dfs(root, root.val)
        return len(good)