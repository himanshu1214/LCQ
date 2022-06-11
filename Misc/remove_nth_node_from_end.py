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

            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        curr = head
        ct = 0
        while curr != None:
            ct += 1
            curr = curr.next
       
        ct -= n 
        print(ct)
        curr = dummy
        while ct > 0:
            ct -= 1
            curr = curr.next

        curr.next = curr.next.next
        return dummy.next
            
        
