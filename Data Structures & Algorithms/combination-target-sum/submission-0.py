class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        the_subset = []

        def dfs(i):
            if i >= len(nums) or sum(the_subset) > target:
                return
            elif sum(the_subset) == target:
                res.append(list(the_subset))
            else:
                the_subset.append(nums[i])
                dfs(i)
                the_subset.pop()
                dfs(i+1)
        dfs(0)
        return res


        