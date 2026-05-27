class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        def recursion(step,remaining):
            if remaining == 0:
                return 1
            elif remaining < 0:
                return 0
            return recursion(step+1,remaining-1) + recursion(step+2,remaining-2)
        return recursion(0,n)