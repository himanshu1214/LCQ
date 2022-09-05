# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        curr = head
        ll = 0
        while curr:
            curr = curr.next
            ll += 1
        curr = head
        nex_head = head.next
        if not nex_head:
            return head
        tmp = ListNode(None)
        if ll % 2:
            while curr.next:
                tmp.next = curr.next
                tmp1 = curr.next
                curr.next = curr.next.next
                tmp1.next = curr
                tmp = curr
                curr = curr.next
        else:
            while curr:
                tmp.next = curr.next
                tmp1 = curr.next
                curr.next = curr.next.next
                tmp1.next = curr
                tmp = curr
                curr = curr.next
              
        return nex_head
