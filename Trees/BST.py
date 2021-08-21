# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Bst:
    def __init__(self):
        self.root = None

    def build_tree(self, node_val):
        if self.root == None:
            self.root = TreeNode(node_val)
        else:
            self._insert(self.root, node_val)

    def _insert(self, curr_node, node_val):
        if curr_node.val > node_val:
            if curr_node.left == None:
                curr_node.left = TreeNode(node_val)
            else:
                self._insert(curr_node.left, node_val)
        else: 
            if curr_node.right == None:
                curr_node.right = TreeNode(node_val)
            else:
                self._insert(curr_node.right, node_val)


    def print_inorder(self):
        if self.root != None:
            self._print(self.root)

    
    def _print(self, curr_node):

        if curr_node != None:
            self._print(curr_node.left)
            print(curr_node.val)
            self._print(curr_node.right)


    def height(self):
        curr = self.root
        ht = 0
        if curr != None:
            ht_val = self.get_height(curr, ht)
            return ht_val

    def get_height(self, curr, ht):
        if curr == None:
            return ht

        left_tree_ht = self.get_height(curr.left, ht+1)

        right_tree_ht = self.get_height(curr.right, ht+1)
        
        return max(left_tree_ht, right_tree_ht)
            
    def search(self, value):
        if value == None:
            return False
        else:
            val = self._search(self.root, value)
        return val
        
    def _search(self, curr, value):
        if curr == None:
            return False
        else:
            if curr.val == value:
                return True


        node_bool =  self._search(curr.right, value) if (curr.val < value) else self._search(curr.left, value)

        return node_bool


tree = Bst()
def fill_tree():
    for i in range(11):
        tree.build_tree(i)
    print("Printing the build tree from here : ")
    tree.print_inorder()
    print(f"Tree Height is : {tree.height()}")
    search_val = 9
    print(f"Value {search_val} is in the tree: {tree.search(search_val)}")

