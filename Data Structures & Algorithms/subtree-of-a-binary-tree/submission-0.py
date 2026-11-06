# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

      self.tree = []
      self.dfs(root)
      arr1 = []
      arr1 += self.tree
      self.tree = []
      self.dfs(subRoot)
      arr2 = []
      arr2 += self.tree

      arr2 = ",".join(arr2)
      arr1 = ",".join(arr1)
      return arr2 in arr1  

    def dfs(self, node):

        if not node:
            self.tree.append("N")
            return
        self.tree.append(str(node.val))
        self.dfs(node.right)
        self.dfs(node.left)

