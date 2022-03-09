class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        products.sort()
        final_list = []
        j =0
        for i in range(1, len(searchWord)+1):
            tmp_list = []
            match = searchWord[:i]
            while len(tmp_list) < 3  and j < len(products):
                if products[j][:i] == match:
                    tmp_list.append(products[j])
                j += 1
            j =0
                
            final_list.append(tmp_list[:])
            
        return final_list
