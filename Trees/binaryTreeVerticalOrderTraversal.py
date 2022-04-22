# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         3 T(0)
        
#  /           \
# 9(0-1)         F 20 (1)
#               /      \
#              15 (1-1)     7(1+1)
    
#  Level ORder Traversal
# At every level -- Queuue - row, col : 3 hashtable 0: 3
#                                                   -1: [9]
#                                                     1: [20]
#                                                     
        if not root:
            return []
        from queue import Queue
        from collections import defaultdict
        q = Queue()
        q.put((root, 0))
        hash_tabl = defaultdict(list)
        while not q.empty():

            size = q.qsize()
            for i in range(size):
                node, index = q.get()
                if node.left:
                    q.put((node.left, index-1))
                if node.right:
                    q.put((node.right, index+1))
                hash_tabl[index].append(node.val)
        _dic = [hash_tabl[k] for k in sorted(hash_tabl)]
        return _dic
