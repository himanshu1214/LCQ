# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        slate = []
        def helper(root, slate):
            if not root:
                slate.append('None')
                return slate
            
            slate.append(str(root.val))
            helper(root.left, slate)
            helper(root.right, slate)
            
            return slate
        
        ser_val = helper(root, [])
        print(ser_val)
        return ",".join(ser_val)
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def helper(l):
            
            if l[0] == 'None':
                l.pop(0)
                return None
                    
            root = TreeNode(l[0])
            l.pop(0)
            root.left = helper(l)
            root.right = helper(l)
            return root
        data_list = data.split(",")
        root = helper(data_list)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
