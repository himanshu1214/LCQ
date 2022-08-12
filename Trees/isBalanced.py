# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]
        def dfs(root):
            if not root:
                return 0 
            
            left = dfs(root.left) + 1
            right = dfs(root.right) + 1
            
            if not res:
                return left
            
            if abs(right - left) > 1:
                res[0] = False
            return max(left, right) 

        dfs(root)
        
        return res[0]
