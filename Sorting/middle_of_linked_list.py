# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        norm_list = []
        ct = 0
        while node != None:
            node = node.next
            ct += 1
            
        nct = (ct//2)+1 if ct%2 == 0 else (ct+1)//2
        
        node = head
        ct = 1
        print(nct)
        if nct == 1:
            return node
        
        while node != None:
            if nct == ct:
                return node
            node = node.next
            ct += 1
            
