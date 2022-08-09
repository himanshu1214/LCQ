# We traverse all the nodes twice so O(N) time complexity
# Space Complexity ~ Stack space in the worst is O(N) and auxilliary space taken is O(k) ~ O(n + k)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        from heapq import heapify, heappush, heappop
        
        max_heap = []
        heapify(max_heap)
        
        def dfs(root):
            if not root:
                return 
            
            if len(max_heap) <k:
                heappush(max_heap, -root.val)
            elif -max_heap[0] > root.val:
                heappop(max_heap)
                heappush(max_heap, -root.val)
                    
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        return -max_heap[0]
    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(root):
            if not root:
                return 
            
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        res.sort()
        return res[k-1]
