class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Is input array sorted? No

        Example:
        [1,3],[2,4],[5,6]
        prev = [1,3]
        curr = [2,4]
        Overlap occurs when prev[1] >= curr[0]
        When an overlap occurs, we want to do the following:
        1. newInterval[0] = prev[0]
        2. newInterval[1] = max(prev[1],curr[1])
        We don't want to append this to the result just yet,
        it can overlap with the next element. Update previous

        Edge Cases:
        len(intervals) < 0
        len(intervals) == 1
        
        [1,3],[2,4],[5,6]
        prev = [1,4]
        curr = [5,6]
        """
        if len(intervals) < 0:
            return []
        if len(intervals) == 1:
            return intervals
        
        sorted_intervals = sorted(intervals,key=lambda x: x[0])
        res = []
        prev = sorted_intervals[0]
        print(prev)
        for interval in sorted_intervals[1:]:
            if prev[1] >= interval[0]:
                prev[1] = max(prev[1],interval[1])
            else:
                res.append(prev)
                prev = interval
        res.append(prev)
        return res


