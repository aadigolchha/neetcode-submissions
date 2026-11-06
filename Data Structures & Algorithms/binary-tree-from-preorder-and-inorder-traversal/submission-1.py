# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_map = {value: i for i, value in enumerate(inorder)}
        preorder_idx = 0

        def build(left_bound, right_bound):
            nonlocal preorder_idx

            if left_bound > right_bound:
                return None

            root = TreeNode(preorder[preorder_idx])
            preorder_idx += 1

            idx = inorder_map[root.val]

            root.left = build(left_bound, idx - 1)
            root.right = build(idx + 1, right_bound)

            return root

        return build(0, len(inorder) - 1)


    
            