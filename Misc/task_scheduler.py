class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import defaultdict
        from heapq import heapify
        task_list = [0 for i in range(26)]
        for i in tasks:
            ch = ord(i) - 65 
            task_list[ch] += 1
        
        task_list.sort()
        max_freq = task_list.pop()
        max_idle_time = (max_freq - 1)*n
        
        print(max_idle_time)
        while task_list and max_idle_time > 0:
            max_idle_time -= min(max_freq -1, task_list.pop())
        max_idle_time = max(0, max_idle_time)
        

        return max_idle_time + len(tasks)
