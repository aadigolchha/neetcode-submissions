class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.vals = []
        self.dfs(k, root)
        print(self.vals)

        return self.vals[k-1]

    def dfs(self, k, root):

        if not root:
            return
        
        if len(self.vals) == k:
            return
        
        self.dfs(k, root.left)
        self.vals.append(root.val)
        self.dfs(k, root.right)