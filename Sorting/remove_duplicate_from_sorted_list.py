# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        prev = head
        nxt = curr.next
        while curr.next != None:
            if nxt.val == curr.val:
                curr = nxt
                nxt = nxt.next
            else:
                prev.next = nxt
                curr = nxt
                prev = nxt
                nxt = nxt.next
        prev.next = None
        return head
                
