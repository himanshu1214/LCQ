class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        l_low = len(str(low))
        l_high = len(str(high))
        sample = "123456789"
        
        comb = []
        start_len = l_low
        while start_len <= l_high:
            start,end = 0, start_len 
            while start <= len(sample) and end <= len(sample):
                comb.append(sample[start:end])
                start += 1
                end += 1
                print(start, end)
            start_len += 1
                
        res = []
        print(comb)
        for i in comb:
            if int(i) >= low and int(i) <= high:
                res.append(i)
        return res
