# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head.next:
            return None
        
        start = head
        F = head
        S = head

        for i in range(n):
            F = F.next

        prev = S
        while F:
            F = F.next
            prev = S
            S = S.next

        if S == head:
            head = head.next
            return head

        prev.next = S.next

        return head
        

        