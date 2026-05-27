class Solution:
    def canFinish(self,numCourses, prerequisites):
        hashmap = defaultdict(list)
        for pre in prerequisites:
            a,b = pre[0],pre[1]
            hashmap[a].append(b)

        visited = set()
        """
        numCourses=5
        hashmap: {
        1:4
        2:4
        3:1,2
        4: []
        }
        dfs(1)
        - visited[1]
        - dfs(4)
          - visited[1,2]
        """
        def dfs(course):
            if course in visited:
                return False
            if hashmap[course] == []:
                return True
            visited.add(course)
            for crs in hashmap[course]:
                if not dfs(crs):
                    return False
            visited.discard(course)
            return True
        for i in range(1,numCourses):
            if not dfs(i):
                return False
        return True