lass Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = [0]
        def dfs(root):
            if not root:
                return False
            
            left = dfs(root.left)
            
            right = dfs(root.right)
            
            val = 0
            if left:
                val += 1
            if right:
                val += 1
            if root.val == p.val or root.val == q.val:
                val += 1
                
            if val >= 2:
                res[0] = root
                return True
            elif val == 1:
                return True
            else:
                return False
            
        dfs(root)
        return res[0]     
