class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visit = set()

        def dfs(node):
            if node in visit:
                return
            
            visit.add(node)

            for nei in graph[node]:
                dfs(nei)

        components = 0

        for node in range(n):
            if node not in visit:
                components += 1
                dfs(node)

        return components