# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def get_depth(root, ct):
            if not root:
                return ct
        
            left_depth = get_depth(root.left, ct+1)
            right_depth = get_depth(root.right, ct+1)
            
            return max(left_depth, right_depth)
            
        return get_depth(root, 0)

    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def get_depth(root):
            if not root:
                return 0
        
            left_depth = get_depth(root.left) + 1
            right_depth = get_depth(root.right) + 1
            
            return max(left_depth, right_depth)
            
        return get_depth(root)

# Alternate
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        global_depth = [0]
        def dfs(root, curr_depth):
            if not root:
                if curr_depth > global_depth[0]:
                    global_depth[0] = curr_depth
                    
                return 
                    
            dfs(root.left, curr_depth +1)
            dfs(root.right, curr_depth +1)
            
            
        dfs(root, 0)
        return global_depth[0]
