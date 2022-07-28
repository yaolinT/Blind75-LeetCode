# There are a total of numCourses courses you have to take, 
# labeled from 0 to numCourses - 1. Y
# ou are given an array prerequisites 
# where prerequisites[i] = [ai, bi] 
# indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], 
# indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
###############################################################
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. 
# So it is possible.

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, 
# and to take course 0 you should also have finished course 1. 
# So it is impossible.
###############################################################

# approach 1(DFS)
# reference: https://www.youtube.com/watch?v=EgI5nU9etnU
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
def canFinish(numCourses, prerequisites):
        temp = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            temp[c].append(p)
        v = set()
        def dfs(c):
            if c in v:
                return False
            if temp[c] == []:
                return True
            v.add(c)
            for p in temp[c]:
                if not dfs(p):
                    return False
            v.remove(c)
            temp[c] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

## Driver code
if __name__=='__main__':
	numCourses, prerequisites = 2, [[1,0]]
	print(canFinish(numCourses, prerequisites))