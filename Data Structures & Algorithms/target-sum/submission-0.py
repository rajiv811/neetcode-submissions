class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        nums - array of int
        target - int

        Problem
        For each num, determine whether to add it or subtract

        Return
        # of unique ways to build expresssion such that total == target
        
        Brute Force
        Recursive backtracking solution
        """
        def recursion(i,count):
            if i == len(nums):
                if count == target:
                    return 1
                else:
                    return 0
            
            return (recursion(i+1,count+nums[i]) + recursion(i+1,count-nums[i]))
        
        return recursion(0,0)
