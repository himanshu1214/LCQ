class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        from collections import defaultdict
        time  = [i%60 for i in time]
        print(time)
        pre = defaultdict(int)
        for i in time:
            pre[i] += 1

        output = 0
        visited = set()
        for k,v in pre.items():
            if k in (0, 30):
                # if k == 0 :
                output += v*(v-1)//2
                # else:
                #     output += v//2
            elif k < 30:
                if (60-k) in pre:
                    output += pre[60-k]*v  
        return output
