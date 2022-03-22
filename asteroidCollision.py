class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        from collections import deque
        stack = deque()
        for i in asteroids:
            print(i)
            while len(stack) and i < 0 and stack[-1] > 0:
                if stack[-1] == -i:
                    stack.pop()
                    break
                    
                elif stack[-1] > -i:
                    break
                    
                
                elif stack[-1] < -i:
                    stack.pop()
                    continue
                    
            else:
                stack.append(i)
            
        return stack
