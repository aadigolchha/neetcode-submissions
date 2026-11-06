# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        l = defaultdict(list)
        height = 0 

        def dfs(root, height):

            nonlocal l        
            if not root:
                return

            l[height].append(root.val)
            dfs(root.left, height + 1)
            dfs(root.right, height + 1)

        dfs(root, 0)
        
        res = []
        for level in l:
            res.append(l[level][-1])
        
        return res
        
        
        
        
        
        
        
        """
        if not root:
            return []

        q = deque()
        q.append(root)

        l = defaultdict(list)

        level = 0
        while len(q) > 0:
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                l[level].append(curr.val)
            
            level += 1
        
        res = []
        for level in l:
            res.append(l[level][-1])
        
        return res
        """
        