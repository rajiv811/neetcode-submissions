class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)

        def backtrack(subarray,visited):
            if len(subarray) == len(nums):
                res.append(subarray.copy())
                return
            for i in range(len(nums)):
                if not visited[i]:
                    subarray.append(nums[i])
                    visited[i] = True
                    backtrack(subarray,visited)
                    subarray.pop()
                    visited[i] = False
        backtrack([],visited)
        return res