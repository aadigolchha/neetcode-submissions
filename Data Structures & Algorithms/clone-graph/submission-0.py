"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        
        q = deque()
        q.append(node)
        clone_start = Node(node.val)
        old_to_new = {node: clone_start}

        while q:
            curr = q.popleft()
            clone = old_to_new[curr]
            for neighbor in curr.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    q.append(neighbor)

                clone.neighbors.append(old_to_new[neighbor])
        return clone_start

       
            

                



