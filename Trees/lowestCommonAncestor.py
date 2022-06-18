# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #             3
        #         /       \
        #     5               1
        #   /    \          /   \         
        # 6       2       0       8
        #       /   \
        #     7       4
        res = [None]
        def helper(root):  
            if root.left:
                left = helper(root.left)
            else:
                left = False
            if root.right:
                right = helper(root.right)
            else:
                right = False
            mid = root == p or root == q            
            if left +mid +right >=2:
                res[0] = root
                
            return left or right or mid
        
        helper(root)
        return res[0]

    
 # Time Complexity O(N)   
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        visited = set()
        output = [0]
        def dfs(root):
            if p.val < root.val and q.val < root.val: 
                return dfs(root.left)
            elif p.val > root.val and q.val > root.val:
                return dfs(root.right)
            else:
                return root


        return dfs(root)
        
