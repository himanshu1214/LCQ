# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.parent = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = [0]
        def dfs(node, par=None):
            if node:
                node.parent = par
                dfs(node.left, node)
                dfs(node.right, node)
                
        dfs(root)
        

        from collections import deque
        node = target
        dq = deque([(target, 0)])

        seen = set()
        seen.add(target)
        while dq:
            if dq[0][1] == k:
                return [node.val for node, d in dq]
            node, dist = dq.popleft()

            for nd in [node.left, node.right, node.parent]:
                if nd and nd not in seen:
                    dq.append((nd, dist+1))
                    seen.add(nd)
        return []
