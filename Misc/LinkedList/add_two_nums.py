# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1  = l1
        node2 = l2
        node3 = ListNode(-1)
        curr_node3 = node3
        rem = 0
        while node1 or node2:
            if not node1:
                val  = (node2.val) + rem
            elif not node2:
                val  = (node1.val) + rem
            else:
                val  = (node1.val + node2.val) + rem
        
            rem = val // 10

            val = val % 10


            print(val, rem)
            tmp = ListNode(val)
            node3.next = tmp
            node3 = node3.next
            if node1:
                node1 = node1.next
            if node2:
                node2 = node2.next
        if rem:
            n = ListNode(rem)
            node3.next = n
        return curr_node3.next
            
