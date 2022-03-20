class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqMap = {i: [] for i in range(numCourses)}
        
        for course, prereq_course in prerequisites:
            prereqMap[course].append(prereq_course)

        visited = set()
        output = []
        cycle = set()
        def dfs(course):

            if course in cycle:
                return False
            
            if course in visited:
                return True
            
            cycle.add(course)
            for prereqs in prereqMap[course]:
                if dfs(prereqs) == False: 
                    return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)

            return True
            
        for crs in range(numCourses):
            if dfs(crs) == False: 
                return []
        return output
