# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        rev_l1 = self.reverselist(l1)
        rev_l2 = self.reverselist(l2)

        s1 = ""
        while rev_l1:
            s1 += str(rev_l1.val)
            rev_l1 = rev_l1.next
        
        s2 = ""
        while rev_l2:
            s2 += str(rev_l2.val)
            rev_l2 = rev_l2.next

        sum = int(s1) + int(s2)
        sum = str(sum)
        
        dummy = ListNode()
        tail = dummy
        for char in sum:
            tail.next = ListNode(char)
            tail = tail.next
        
        return self.reverselist(dummy.next)



    def reverselist(self, head: Optional[ListNode]):

        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

            
