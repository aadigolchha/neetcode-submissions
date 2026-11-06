# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        next = []
        next.append(root)
        result = root

        while next:

            node = next.pop()

            node.left, node.right = node.right, node.left
            
            if node.left:
                next.append(node.left)
                
            if node.right:
                next.append(node.right)
            
        return result



                