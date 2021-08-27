# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        def helper(curr):
            if not curr:
                return 
            result.append(curr.val)
            helper(curr.left)
            helper(curr.right)
            

            return result
        
        helper(root)
        return result
