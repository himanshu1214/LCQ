# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from heapq import heapify, heappush, heappop
        min_heap = []
        
        #this will capture all the nodes in min heap
        head = ListNode(None)
        for list_ in lists:
            curr = head
            while list_ is not None:
                heappush(min_heap, list_.val)
                list_ = list_.next
                
        print(min_heap)
        # create a sorted linked list
        head = ListNode(None)
        curr = head
        while min_heap:
            curr.next = ListNode(heappop(min_heap))
            curr = curr.next
            
        return head.next
            
        
