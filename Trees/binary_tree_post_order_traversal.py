"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        result = []
        def helper(curr):
            if not curr:
                return 
            for ch in curr.children:
                helper(ch)
                result.append(ch.val)

        helper(root)
        result.append(root.val)
        return result
