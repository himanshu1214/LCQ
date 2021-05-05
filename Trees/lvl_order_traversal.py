# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = queue.Queue()
        result = []
        q.put(root)
        while not q.empty():
            numnodes= q.qsize()
            temp = []
            i=0
            while i < numnodes:
                node = q.get()
                temp.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
                i += 1
            result.append(temp)
        return result
            
        
        
