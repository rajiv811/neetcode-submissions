class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        How do we know if it's a valid tree? 2 cases:
        1. Is there a cycle? If so, not valid
        2. Is the graph connected? If not, not valid

        Edge case: How do we avoid detecting a cycle if two nodes are connected? E.g. [0,1] and [1,0] - add code to skip over this

        Solution: modified DFS
        Data structures: List to represent node and it's neighbors, set to detect visited nodes
        """
        if len(edges) > (n-1):
            return False
        visited = set()
        adjacent = [[] for _ in range(n)]
        # let index represent node, value is neighbors

        for f,s in edges:
            adjacent[f].append(s)
            adjacent[s].append(f)
        
        def dfs(node,prev):
            if node in visited:
                return False
            visited.add(node)
            for nei in adjacent[node]:
                if nei == prev:
                    continue
                else:
                    if not dfs(nei,node):
                        return False
            return True
        return dfs(0,-1) and len(visited) == n
