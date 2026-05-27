class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Try removing each edge from the back.
        If the remaining graph has no cycle, then that removed edge
        is the redundant connection.
        """

        def isCycle(visited, edge_list):
            n = len(edges)
            adj = [[] for _ in range(n + 1)]

            for u, v in edge_list:
                adj[u].append(v)
                adj[v].append(u)

            def dfs(node, parent):
                visited.add(node)

                for nei in adj[node]:
                    if nei == parent:
                        continue
                    if nei in visited:
                        return True
                    if dfs(nei, node):
                        return True
                return False

            for node in range(1, n + 1):
                if node not in visited:
                    if dfs(node, -1):
                        return True
            return False

        for i in range(len(edges) - 1, -1, -1):
            modified_edges = edges[0:i] + edges[i+1:]
            if not isCycle(set(), modified_edges):
                return edges[i]

        return []