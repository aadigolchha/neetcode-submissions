# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #find middle
        F = head
        S = head
        S_prev = S

        while F and F.next:
            F = F.next.next
            S_prev = S
            S = S.next
        
        S_prev.next = None

        #reverse second half
        reverse_h2 = self.reverse_list(S)

        #interleave
        tail = reverse_h2
        while head and reverse_h2:
            val1 = head.next
            val2 = reverse_h2.next
            head.next = reverse_h2
            reverse_h2.next = val1
            head = val1
            tail = reverse_h2
            reverse_h2 = val2

        if reverse_h2:
            tail.next = reverse_h2
        
            




        
    
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev