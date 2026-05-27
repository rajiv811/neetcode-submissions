class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        brute force
        """
        def dfs(i):
            if i >= len(nums) - 1:
                return True  # reached or passed the end
            for nxt in range(i + 1, i + nums[i] + 1):
                if dfs(nxt):
                    return True
            return False
        return dfs(0)
