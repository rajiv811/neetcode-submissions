class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 1. Make decision
        # 2. Continue making decision until you come across invalid res
        # 3. Backtrack and make different decision
        res = []
        def backtrack(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # Include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            # Exclude nums[i]
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res