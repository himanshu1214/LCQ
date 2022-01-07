# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.ln = self.gen_ln()
    
    def gen_ln(self):
        node = self.head
        ln = 0
        while node:
            ln += 1
            node = node.next
        return ln
        
    def getRandom(self) -> int:
        rand_pos = random.randint(1, self.ln)
        node = self.head
        ln = 0
        while node:
            ln += 1
            print(node.val)
            if ln == rand_pos:
                return node.val
 
            node = node.next            

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
