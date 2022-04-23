# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def helper(node, low, high):
            if not node:
                return 0

            left = helper(node.left,low, high)
            right = helper(node.right, low, high)
            
            if node.val >= low and node.val <= high:
                
                return left + right +  node.val
            else:
                return left + right
            
        res = helper(root, low, high)
        return res
        
