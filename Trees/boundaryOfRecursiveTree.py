# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def left_nodes(node):
            if not node.left and not node.right:
                return 
            
            res.append(node.val)
            if node.left:
                left_nodes(node.left)
            elif node.right:
                left_nodes(node.right)

                    
        def bottom_leaves(node):
            if not node:
                return 
            
            if node.left:
                bottom_leaves(node.left)
                
            if node != root and not node.left and not node.right:
                res.append(node.val)
                
            if node.right:
                bottom_leaves(node.right)
                
            
        def right_nodes(node):
            if not node.left and not node.right:
                return 
            
            if node.right:
                right_nodes(node.right)
            elif node.left:    
                right_nodes(node.left)
            
            res.append(node.val)
    
        res.append(root.val)
        
        if root.left:
            left_nodes(root.left)
        bottom_leaves(root)
        if root.right:
            right_nodes(root.right)
        return res
