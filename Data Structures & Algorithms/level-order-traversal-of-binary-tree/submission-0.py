# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        q = deque()
        q.append(root)

        res = defaultdict(list)

        height = 0
        while len(q) > 0:
            for i in range(len(q)):
                curr = q.popleft()
                res[height].append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            height += 1

        arr = [[] for _ in res.keys()]

        for key in res:
            arr[key].extend(res[key])

        return arr



