"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return

        val = defaultdict()
        tail = head
        
        while tail:
            val[tail] = Node(tail.val)
            tail = tail.next

        tail2 = head

        while tail2:
            if tail2.next:
                val[tail2].next = val[tail2.next]
            if tail2.random:
                val[tail2].random = val[tail2.random]
            tail2 = tail2.next
        
        return val[head]


