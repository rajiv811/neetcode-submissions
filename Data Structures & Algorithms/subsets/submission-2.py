class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Decision Tree
        At every decision, you can either add num or not.
        The num is dependent on what index of nums you are search
        """

        res = []

        def backtracking(decisions,subset):
            if decisions >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[decisions])
            backtracking(decisions+1,subset)

            subset.pop()
            backtracking(decisions+1,subset)

        
        backtracking(0,[])
        return res