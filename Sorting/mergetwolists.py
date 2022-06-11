# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        from heapq import heappush, heappop, heapify
        min_heap = []
        heapify(min_heap)
        
        curr = list1
        while curr:
            heappush(min_heap, curr.val)
            curr = curr.next
            
        curr = list2
        while curr:
            heappush(min_heap, curr.val)
            curr = curr.next
            
        start = 0 
        end = len(min_heap)
        head = ListNode(None)
        curr = head 
        
        print(len(min_heap))
        while start < end:
            tmp = ListNode(heappop(min_heap))
            curr.next = tmp
            curr = curr.next
            start += 1
        return head.next
