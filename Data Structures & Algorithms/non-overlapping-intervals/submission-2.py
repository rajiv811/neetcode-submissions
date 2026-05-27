class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return None
        intervals.sort(key = lambda x: x[0])
        # [1,2] [1,4] [2,4]

        res = 0
        prev = intervals[0]
        for interval in intervals[1:]:
            # This is an overlap
            if prev[1] > interval[0]:
                res += 1
                if prev[1] > interval[1]:
                    prev = interval
            else:
                prev = interval
        
        return res