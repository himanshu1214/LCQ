# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        from collections import defaultdict
        rs = defaultdict(int)
        curr = head
        index = 0
        while curr:
            curr = curr.next
            index += 1
            
        n = index
        curr = head
        index = 0

        while curr:
            if n-1 - index in rs:
                rs[n-1-index] += int(curr.val)
            else:
                rs[index] = int(curr.val)
            curr =  curr.next
            index += 1
            
        return max(rs.values())
