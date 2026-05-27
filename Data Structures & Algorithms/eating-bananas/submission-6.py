class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        piles[i] - num bananas in pile i
        h - num hours you HAVE to finish bananas within
        k - bananas/hour that can finish all piles

        Constraints
        Can only eat at 1 pile at a time

        Return
        Min k
        """
        """
        Binary Search
        """
        l,r = 1,max(piles)
        min_k = max(piles)
        while l <= r:
            mid = (r+l) // 2
            curr_h = 0
            for pile in piles:
                curr_h += math.ceil(pile / mid)
            if curr_h > h:
                l = mid + 1
            else:
                min_k = min(min_k,mid)
                r = mid - 1
        return min_k

        """
        Brute Force
        piles = [5,5,5,5,5] h = 5
        1 <= k <= 5
        piles = [1,4,3,2], h = 9
        """
        min_count = max(piles)
        for i in range(1,max(piles)):
            count = 0
            for pile in piles:
                count += math.ceil(pile / i)
            if count <= h:
                min_count = min(i,min_count)
        return min_count
