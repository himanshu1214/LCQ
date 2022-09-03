class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        while start < len(temperatures):
            
            while stack and temperatures[stack[-1]] < temperatures[start]:
            
                # Pop untill the temperature is colder
                i = stack.pop()
                res[i] = (start - i)
            # add into stack untill the next warmer temperature  
            stack.append(start)
            start += 1
        
        return res
