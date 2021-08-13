class Node():
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = Node() #placeholder for header pointer
        
    def append(self, node):
        new_node = Node(node)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        len_list = 0 
        while cur.next != None:
            cur = cur.next
            len_list += 1
        return len_list

    def print_list(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
            print(cur.val)


    def get(self, index):
        if index >= self.length():
            raise IndexError("Index Out Of Range")
        cur = self.head
        ct = 0
        while cur.next != None:
            cur = cur.next
            if ct == index:
                break
            ct += 1        
        return cur.val 
    
    def remove(self, index):
        if index >= self.length():
            raise IndexError("Index Out Of Error")
        cur = self.head
        cur_indx = 0
        prev_ptr = self.head
        while cur.next != None:
            if index == cur_indx:
                prev_ptr.next = cur.next.next
                return 
            prev_ptr = cur.next
            cur = cur.next
            cur_indx += 1


