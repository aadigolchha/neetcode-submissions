# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.preorder_list = []
        self.preorder(root)
        return ",".join(self.preorder_list)

    def preorder(self, root):
        if not root:
            self.preorder_list.append("N")
            return

        self.preorder_list.append(str(root.val))
        self.preorder(root.left)
        self.preorder(root.right)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        values = data.split(",")
        preorder_idx = 0

        def build():
            nonlocal preorder_idx

            if values[preorder_idx] == "N":
                preorder_idx += 1
                return None

            node = TreeNode(int(values[preorder_idx]))
            preorder_idx += 1

            node.left = build()
            node.right = build()

            return node

        return build()

