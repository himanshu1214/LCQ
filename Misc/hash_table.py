
class Bucket:
    def __init__(self):
        self.bucket = []
    
    def update(self, key, val):
        for ind, kval in enumerate(self.bucket):
            ky , vl = kval[0], kval[1] 
            if ky == key:
                self.bucket[ind] = (key, val)
                return
            
        self.bucket.append((key, val))
    
    def get(self, key):
        for k, v in self.bucket:
            if k == key:
                return v

        return -1
    
    def remove(self, key):
        for ind, kv in enumerate(self.bucket):
            ky, vl = kv[0], kv[1]
            if ky == key:
                self.bucket.pop(ind)
                return
        

class MyHashMap:

    def __init__(self):
        self.key_space = 2069
        self.hash_table = [Bucket() for i in range(self.key_space)]
    
    
    def hash_func(self, key):
        return key % self.key_space

    def put(self, key: int, value: int) -> None:
        hash_val = self.hash_func(key)
        # print(hash_val)
        self.hash_table[hash_val].update(key, value)
        
    def get(self, key: int) -> int:
        hash_val = self.hash_func(key)
        return self.hash_table[hash_val].get(key)
        
    
    def remove(self, key: int) -> None:
        hash_val = self.hash_func(key)
        self.hash_table[hash_val].remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
