# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        #Tree 
           #                root 
        #       left                        rght
        # left(leaf, Base) right        left   right (Base)
        #lval                               rval
        if not root:
            return None
        import sys
        res = [0]
        def helper(root):
            if not root: return sys.maxsize , -sys.maxsize
            if (root.left==None) and  (root.right==None): 
                return root.val, root.val
            
            lval = helper(root.left)
            rval = helper(root.right)
            
            min_ = min(lval[0], rval[0])
            max_ = max(lval[1], rval[1])
            
            res[0] = max(res[0], abs(root.val - min_), abs(root.val - max_))
            
            min_ = min(min_, root.val)
            max_ = max(max_, root.val)
            return min_, max_
        
        helper(root)
        return res[0]
