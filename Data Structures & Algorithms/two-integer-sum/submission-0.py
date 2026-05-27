class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #key = num, val = index

        d = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in d:
                return [d[diff],i]
            d[n] = i
            
        
