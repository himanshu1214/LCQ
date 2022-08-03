# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr =  ListNode(None)
        curr.next = head
        m = 0
        while curr:
            m += 1
            curr = curr.next
            
        curr =  ListNode(None)
        curr.next = head
        _curr = curr
        n = m-n
        
        while n>0:
            prev = _curr
            _curr = _curr.next
            n -= 1

        prev.next = _curr.next
        
        return curr.next
