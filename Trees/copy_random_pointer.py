# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

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
