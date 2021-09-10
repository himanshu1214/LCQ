class Solution: #Overflowing for 10^9. Check it back
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # if h == 1000000000 and w == 1000000000:
        #     return 64
            
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.append(w)

        res = [[0 for j in range(len(verticalCuts))] for i in range(len(horizontalCuts))]
        print(res)

        for num_i, i in enumerate(horizontalCuts):
            for num_j, j in enumerate(verticalCuts):
                if num_j== 0 and num_i==0:
                    res[num_i][num_j] = i*j

                elif num_j ==0 and num_i>0:
                        res[num_i][num_j] = (i- horizontalCuts[num_i-1])*j
                elif num_i == 0 and num_j>0:
                    res[num_i][num_j] = (j- verticalCuts[num_j-1])*i

                elif num_i> 0 or num_j>0:
                    res[num_i][num_j] = (j- verticalCuts[num_j-1])*(i- horizontalCuts[num_i-1])
        f_res = []
        for i in res:
            f_res.extend(i)

        return max(f_res)% (10**9 + 7)
