"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        result = [root.val]
        def helper(curr):
            if not curr:
                return 
            for ch in curr.children:
                result.append(ch.val)
                helper(ch)
            
        helper(root)
        return result
            
        
