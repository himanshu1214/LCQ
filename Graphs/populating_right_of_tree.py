# Dec 29 Daily
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        from queue import Queue

        # final_list = []
        q = Queue()
        curr_node = root
        q.put(curr_node)
        prev_node = None
        while not q.empty():
            n_ln = q.qsize()
            # print(n_ln)
            for i in range(n_ln):
                curr_node = q.get()
                # print(curr_node.val)
                if curr_node.left:
                    q.put(curr_node.left)
                    q.put(curr_node.right)
                if prev_node:
                    prev_node.next = curr_node
                    # print(f"NEXT: {prev_node.val}")
                
                prev_node = curr_node
                print
            curr_node.next = None
            prev_node = None
        return root
