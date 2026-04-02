class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visit = set()

        def dfs(node, parent):
            if node in visit:
                return

            visit.add(node)

            for nei in graph[node]:
                if nei == parent:
                    continue
                dfs(nei, node)

        dfs(0, -1)
        return len(visit) == n