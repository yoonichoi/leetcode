class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        visited = [0 for _ in range(n)]
        for connection in edges:
            x,y = connection
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(graph, visited, i):
            if visited[i]: return
            visited[i] = 1
            for j in graph[i]:
                dfs(graph, visited, j)
        
        cnt = 0
        for i in range(n):
            if not visited[i]:
                dfs(graph, visited, i)
                cnt += 1
        return cnt