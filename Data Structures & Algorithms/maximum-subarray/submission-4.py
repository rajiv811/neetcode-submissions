class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Brute Force - Look through every subarray and keep track of max
        """
        # max_sub = nums[0]
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(i,len(nums)):
        #         count += nums[j]
        #         max_sub = max(max_sub,count)
        # return max_sub

        """
        How do we optimize brute force?
        nums = [2,-3,4,-2,2,1,-1,4]
        2 -> -1 -> 3
        We DON'T want to keep track of negative sums. Why?
        - it will never be the max. If a sum is negative, there will always
        be a smaller value
        2 -> -1: Update window to:
        [4,-2,2,1,-1,4]
        4 -> 2 -> 4 -> 5 -> 4 -> 8
        """
        """
        Walk through code:
        [4,-2,2,1,-1,4]
        Kadane's Algorithm
        """
        max_sub = nums[0]
        curr = nums[0]
        for i in range(1,len(nums)):
            if curr < 0:
                curr = 0
            curr += nums[i]
            max_sub = max(max_sub,curr)
        return max_sub