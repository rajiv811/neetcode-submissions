class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Steps
        1. Find pivot
        2. Run binary search on l:pivot-1 and pivot:r

        [3,4,5,6,1,2]
        """

        l,r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l

        def binary_search(l,r):
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] == target:
                    return mid
                
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        
        res = binary_search(0,pivot-1)
        if res != -1:
            return res
        return binary_search(pivot,len(nums)-1)