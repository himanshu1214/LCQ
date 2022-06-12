# Time Complexity
# Since we traverse each node no more than once ~ O(n)
# Space Complexity
# At a time max stack can be of length ~ log (N) or worst case it is O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Three step process:
        # Step 1: For each node begining from root:
        # Path :  left --> root --> right (here split is allowed)
        # Going downward --> We have to choose either left or right and that will included 
        # Ex:         1
#                   /   \
#                 2       3
#                       /   \
#                      4     5
# Our possible path can be with root 3: 4 --> 3 --> 5
# Or with root --> we can choose 2 --> 1 --> (3 --> (4 or 5))
# Using DFS --> we get the  3 + 4 + 5 = 12 for root 3 (thats max at this level) return can root + max(left, right) {we can either choose left or right} >> 3 + (4, 5) --> 8
# Calculate val for root 1 >> 2 + 1 + 8 = 11 
# Globally max at this node (11, 12) --> 12

        res = [float('-inf')]
        def dfs(root):
            
            if not root:
                return 0
            
            lft = max(dfs(root.left), 0)
            
            rht = max(dfs(root.right), 0)
            
            _tot = root.val + lft + rht
            if _tot> res[0]:
                res[0] = _tot
            tot = root.val + max(lft, rht)
            return tot
        
        dfs(root)
        return res[0]
            
