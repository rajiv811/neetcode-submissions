class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Think of it as a directed acyclic graph
        1. Identify Type of DP Problem : Asking for OPTIMAL result (longest length)
        2. Define the state : state is the smallest set of parameters 
           needed to describe any subproblem
           dp[i] = length of the longest increasing subsequence ending at index i
        3. dp[i] = 1 + max(dp[j] for all j < i where nums[j] < nums[i])
        4. Base case: dp[i] = 1  for all i
        5. dp[i] depends on dp[j] where j < i → process from left to right.
           Outer loop over i, inner loop over j.
        6. Result : result = max(dp)
        """
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n  # dp[i] = length of LIS ending at i
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)