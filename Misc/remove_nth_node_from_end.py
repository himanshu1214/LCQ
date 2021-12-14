# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        ct = 0
        while node != None:
            node = node.next
            ct += 1
            
        stop_node = ct - n 
        
        node = head
        print(stop_node)
        ct = 0
        
        while node != None:
            if stop_node == 0:
                if node.next is not None:
                    print(node.val, head.val)
                    
                    return head.next
                else:
                    return head.next
            
            ct += 1
            if stop_node == ct:
                node.next = node.next.next
                return head
            node = node.next

            
            
        
