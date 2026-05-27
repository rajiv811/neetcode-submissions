class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Cannot sort
        count = 0
        set_nums = set(nums)

        for i in range(len(nums)):
            temp_count = 0
            j = i
            if (nums[j] - 1) not in set_nums:
                while j < len(nums) and nums[j] + temp_count in set_nums:
                    temp_count += 1
                count = max(count,temp_count)
        return count