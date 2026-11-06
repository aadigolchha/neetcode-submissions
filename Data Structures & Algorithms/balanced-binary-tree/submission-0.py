# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:

        height, balanced = self.dfs(root)
        return balanced

    def dfs(self, root) -> (int, bool):

        if not root:
            return (0, True)
        
        right = self.dfs(root.right)
        left = self.dfs(root.left)

        height = max(right[0], left[0])

        balanced = (abs(right[0] - left[0]) <= 1) and (right[1] and left[1])

        return (1 + height, balanced)