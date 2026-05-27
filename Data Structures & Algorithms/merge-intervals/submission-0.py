class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Is it sorted? If not, sort on the first element
        # For loop i -> len(intervals) - 2

        if not intervals:
            return None
        
        intervals.sort(key = lambda x: x[0])

        prev = intervals[0]
        res = []
        for interval in intervals[1:]:
            if prev[1] >= interval[0]:
                prev = [
                    prev[0],
                    max(interval[1],prev[1])
                ]
            else:
                res.append(prev)
                prev = interval
        res.append(prev)
        return res

            
            
