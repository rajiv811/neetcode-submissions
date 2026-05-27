class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # b is the pre-req, need to complete b before taking a
        # build map of course: pre-req, run dfs through map. If you
        # go to a node you've already seen before, return False (cycle)
        m = defaultdict(list)
        for pre in prerequisites:
            a,b = pre[0],pre[1]
            m[a].append(b)
        visited = set()
        def dfs(i):
            if i in visited:
                return False
            if m[i] == []:
                return True
            visited.add(i)
            for crs in m[i]:
                if not dfs(crs):
                    return False
            visited.discard(i)
            return True
        for i in range(1,numCourses):
            if not dfs(i):
                return False
        return True
