# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        self.tree1 = []

        self.dfs(p)
        arr1 = []
        arr1 += self.tree1
        print(self.tree1)

        self.tree1 = []
        self.dfs(q)
        arr2 = []
        arr2 += self.tree1
        print(self.tree1)

        return arr1 == arr2


    def dfs(self, node):

        if not node:
            self.tree1.append(None)
            return

        self.tree1.append(node.val)
        self.dfs(node.left)
        self.dfs(node.right)



        
