class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary Search
        l,r = 1, max(piles)
        res = r

        while l <= r:
            mid_speed = (r + l) // 2
            hour = 0
            for p in piles:
                hour += math.ceil(float(p) / mid_speed)
            if hour <= h:
                res = min(mid_speed,res)
                r = mid_speed-1
            else:
                l = mid_speed+1
        return res
        #Brute Force
        """
        speed = 1
        while True:
            hour = 0
            for pile in piles:
                hour += math.ceil(pile / speed)
            if hour == h:
                return speed
            speed += 1
        return speed
        """
                        
                