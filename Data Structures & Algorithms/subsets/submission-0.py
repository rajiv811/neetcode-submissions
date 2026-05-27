class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr_sequence = []

        def dfs(res,curr_sequence,i):
            if i >= len(nums):
                res.append(list(curr_sequence))
                return
            curr_sequence.append(nums[i])
            dfs(res,curr_sequence,i+1)

            curr_sequence.pop()
            dfs(res,curr_sequence,i+1)
        
        dfs(res,curr_sequence,0)
        return res
        