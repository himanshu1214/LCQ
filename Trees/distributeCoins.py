# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None, parent=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.parent = parent
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.num_moves = 0
        
        def helper(node):
            if not node:
                return 0
            l = helper(node.left)
            r = helper(node.right)
            
            self.num_moves += abs(l)+ abs(r)
            
            return node.val + l  + r -1
        helper(root)        
        return self.num_moves
    
        
