class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        1. Use binary search to find pivot
        2. Find which half of the list the target is in (left or right)
        3. Run binary search on the already sorted half
        time complexity: O(log n) + O(log n) = O(log n)
        # [3,1,2]
        """
        l,r = 0, len(nums)-1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pivot = l

        l,r = 0, len(nums) - 1
        if target <= nums[r] and target >= nums[pivot]:
            l = pivot
        else:
            r = pivot - 1
        
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


        
