class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       # Binary Search
        l,r = 1,max(piles)
        res = r
        while l <= r:
            mid = (l+r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / mid)
            if hours <= h:
                res = min(res,mid)
                r = mid-1
            else:
                l = mid+1
        return res
       
       # Brute Force Approach
        res = max(piles)
        for i in range(1,max(piles)):
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / i)
            if hours <= h:
                res = min(res, i)
        return res