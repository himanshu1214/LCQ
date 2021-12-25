# GooGLE Interview Q : medium
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(set(fruits)) <= 2:
            return len(fruits)
        start, end = 0, 1
        ln = 0
        basket = []
        while end <= len(fruits):
            if len(set(fruits[start:end])) <=2:
                if len(fruits[start:end]) > ln:
                    ln = len(fruits[start:end])
                end += 1
            else:
                start += 1
        return ln
