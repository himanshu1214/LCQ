# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node = head
        visited = {}
        def helper(head):
            if not head:
                return None
            
            node = Node(head.val, None, None)
            if head not in visited:
                visited[head] = node
            else:
                return visited[head]
           
            _next = helper(head.next)
            _random = helper(head.random)
                
            node.next = _next
            node.random = _random
            
            return node
        
        return helper(head)


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        #1. Iterate to point the next pointer of original to clone pointer
        # 2. Weaveing - >Iterate to point the random pointer of original next to cloned random pointer
        # 3. Unweave it 
        
        # Step 1
        original = head
        while original:
            node = Node(original.val, None, None)
            node.next = original.next 
            original.next = node
            original = node.next    
        
        # Step 2:
        # Weaveit
        original = head
        while original:
            original.next.random = original.random.next if original.random is not None else None
            original = original.next.next
            
        # Unweave it Step 3
        old_ptr = head
        new_ptr = head.next
        head_new = head.next
        while old_ptr:
            old_ptr.next = old_ptr.next.next if old_ptr.next is not None else None
            new_ptr.next = new_ptr.next.next if new_ptr.next is not None else None
            
            old_ptr = old_ptr.next
            new_ptr = new_ptr.next
        return head_new
            
