# Since we are traversing each node twice O(N)
# space Complexity at worst the stack spaace is O(N) for skewed tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder (node-> left --> right) inorder (left -> node -> right)
        # preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]                    
        #                       3(root)
        
        def helper(preorder, inorder):
            if not preorder or not inorder:
                return None
        
            val = preorder.pop(0)
            node = TreeNode(val)
            ind = inorder.index(val)
            node.left = helper(preorder, inorder[:ind])
            node.right = helper(preorder, inorder[ind+1:])
            return node
        
        return helper(preorder, inorder)
