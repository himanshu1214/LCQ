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
            
 # Time Complexity : O(N) we encountered the node only once 
# Space Complexity : O(N) we capture all the nodes 
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from queue import Queue
        
        def bfs(root):
            if not root:
                return
            q = Queue()
            lvl_order = []
            q.put(root)
            while not q.empty():
                tot_node = q.qsize()
                tmp = []
                for i in range(tot_node):
                    _node = q.get()
                    if _node.left:
                        q.put(_node.left)
                    if _node.right:
                        q.put(_node.right)
                    tmp.append(_node.val)
                lvl_order.append(tmp)
            
            return lvl_order
        
        return bfs(root)

# Alternate

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from queue import Queue
        if not root:
            return []
        
        def bfs(root):
            q = Queue()
            q.put(root)
            res = []
            while not q.empty():
                siz = q.qsize()
                tmp = []
                for i in range(siz):
                    node = q.get()
                    if node.left:
                        q.put(node.left)

                    if node.right:
                        q.put(node.right)
                        
                    tmp.append(node.val)
                    
                res.append(tmp)
            return res
        
        return bfs(root)
        
