# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        F = head
        S = head

        while F and F.next:
            F = F.next.next
            S = S.next
            if F == S:
                return True

        return False

            