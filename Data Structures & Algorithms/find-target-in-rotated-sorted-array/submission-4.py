class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        """
        [3,4,5,6,1,2]
        l = 3, m = 5, r = 2
        [6,1,2]
        l = 6, m = 1, r = 2
        [6,1]
        l = 6, m = 6, r = 1
        [1]
        """
        while l < r:
            mid = (l+r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        pivot = l

        # Figure out which side to do binary search on
        """
        [3,4,5,6,1,2] target = 1
        """
        l,r = 0,len(nums)-1
        if  target > nums[pivot] and target > nums[r]:
            r = pivot - 1
        else:
            l = pivot
        
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
