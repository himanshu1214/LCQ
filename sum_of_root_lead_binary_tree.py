# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = []
        def helper(root, slate):
            
            if not root.left and not root.right:
                slate.append(root.val)
                res.append(slate[:])
                slate.pop()
                return
            
            if root.left:
                slate.append(root.val)
                helper(root.left, slate)
                slate.pop()
            if root.right:
                slate.append(root.val)
                helper(root.right, slate)
                slate.pop()
            
            
        helper(root,[])
        int_val = 0
        res = [[str(i) for i in rs] for rs in res]
        for rs in res:
            val = ''.join(rs)
            _v = int(val, 2)
            int_val += _v
        return int_val
        
