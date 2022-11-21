class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for a,b in prerequisites:
            prereq[a].append(b)
        def dfs(i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
            visited[i] = -1
            for j in prereq[i]:
                if not dfs(j):
                    return False
            visited[i] = 1
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
  