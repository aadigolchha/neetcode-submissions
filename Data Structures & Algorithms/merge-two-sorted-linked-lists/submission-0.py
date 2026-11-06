class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1: return list2
        if not list2: return list1

        sorted_tail = ListNode()
        sort = sorted_tail
        while list1 and list2:
            if list1.val <= list2.val:
                sorted_tail.next = list1
                list1 = list1.next
                sorted_tail = sorted_tail.next

            else:
                sorted_tail.next = list2
                list2 = list2.next
                sorted_tail = sorted_tail.next

        if list1 and not list2:
            sorted_tail.next = list1
        if list2 and not list1:
            sorted_tail.next = list2

        return sort.next
        