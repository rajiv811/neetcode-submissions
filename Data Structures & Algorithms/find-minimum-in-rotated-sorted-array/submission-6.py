class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Case 1:
        [3,4,5,6,1,2]
        l = 3, mid = 5, r = 2
        if r < mid: pivot occurs somewhere betwen mid + 1 and r. l = mid + 1
        Case 2:
        [3,1,2]
        if r > mid:
            r = mid

        Walk Through:
        [3,4,5,6,1,2]
        l = 3, r = 2, mid = 5
        2 < 5
        [6,1,2]
        l = 6, r = 2, mid = 1
        [6,1]
        l =6, r = 1, m = 6

        nums=[2,1]
        l = 2, r = 1, m = 2
        [1]
        """
        if len(nums) == 1:
            return nums[0]
        l,r = 0, len(nums)-1
        the_min = float("inf")

        while l < r:
            mid = (l+r) // 2
            the_min = min(the_min,nums[mid])

            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid
        
        return min(the_min,nums[l])