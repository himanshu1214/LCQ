# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, k):
            """Return the reversed head"""
            prev= None
            curr = head
            while k:
                tmp =  curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                k -= 1
            return prev
        
        def helper(head):
            ptr = head
            count = 0
            while count < k and ptr:
                count += 1
                
                ptr = ptr.next

            if count == k:
                
                reversed_head = reverse(head, k)
        
                head.next = helper(ptr)
                return reversed_head
