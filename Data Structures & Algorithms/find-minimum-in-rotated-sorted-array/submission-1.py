class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        # have to determine which side to shrink to when you get mid
        # [3,4,5,6,1]

        l,r = 0, len(nums)-1
        the_min = float("inf")
        while l < r:
            mid = (l+r) // 2
            the_min = min(the_min,nums[mid])
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return min(the_min,nums[l])