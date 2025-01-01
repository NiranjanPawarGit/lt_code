from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        crs = prerequisites
        g = defaultdict(list)

        # Build the graph
        for a, b in crs:
            g[a].append(b)

        VISITED = 2
        VISITING = 1
        UNVISITED = 0

        states = [0] * numCourses

        def dfs(i):
            if states[i] == VISITING:  # Cycle detected
                return False
            if states[i] == VISITED:  # Already checked, no cycle here
                return True

            states[i] = VISITING  

            
            for nei in g[i]:
                if not dfs(nei):  
                    return False

            states[i] = VISITED  
            return True

        # Check all courses for cycles
        for i in range(numCourses):
            if not dfs(i):  
                return False
        return True 

# Example to test the Solution class
solution = Solution()

# Example 1: Can finish all courses (no cycle)
numCourses = 2
prerequisites = [[1, 0]]  # Course 1 depends on course 0
print(solution.canFinish(numCourses, prerequisites))  # Expected output: True

# Example 2: Cannot finish all courses (cycle exists)
numCourses = 2
prerequisites = [[1, 0], [0, 1]]  # Course 1 depends on course 0, and course 0 depends on course 1 (cycle)
print(solution.canFinish(numCourses, prerequisites))  # Expected output: False
