# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# TODO
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        prev, curr = dummy, head
        prev.next = head
        
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
                
            if prev.next == curr:
                prev, curr = prev.next, curr.next
            else:
                prev.next = curr.next
                curr = prev.next
                
        return dummy.next
