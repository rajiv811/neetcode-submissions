class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        h_map = {i:[] for i in range(numCourses)}
        for non_pre,pre in prerequisites:
            h_map[non_pre].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                # Cycle!
                return False
            if h_map[crs] == []:
                return True
            visiting.add(crs)
            for pre in h_map[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            h_map[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            