class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy
        import heapq
        min_heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i))
        
        while min_heap:
            val, idx = heapq.heappop(min_heap)
            tail.next = lists[idx]
            tail = tail.next
            lists[idx] = lists[idx].next
            if lists[idx]:
                heapq.heappush(min_heap, (lists[idx].val, idx))
                
        return dummy.next