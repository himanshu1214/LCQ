# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Step 1
        # Find the middle of  linked list using  slow and fast pointer
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next    
        
        # Step2:
        # Reverse the linkedin list for the second part 
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # Step 3:
        # Merge the first part and second one by one 
        first, second = head, prev
        while second:
            tmp_first = first.next
            tmp_second = second.next
            first.next = second
            second.next = tmp_first
            first, second = tmp_first, tmp_second
            
