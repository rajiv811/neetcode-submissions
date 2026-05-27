class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Description
        We are given sorted intervals. Add newInterval

        Var
        intervals - list of intervals in sorted order
        newInterval - new interval to add

        Constraints
        If the interval overlaps, resolve overlap by merging 
        said intervals.

        Solution
        Walk through list. If you encounter an overlap, pop element
        and resolve overlap. append merged interval.

        Edge Cases:
        """
        if len(intervals) < 1:
            return [newInterval]
        res = []
        for i in range(len(intervals)):
            # If newInterval is less than current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res += intervals[i:]
                return res
            # If newInterval is greater than current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # If there is an overlap, merge intervals. Update newInterval
            else:
                newInterval[0] = min(newInterval[0],intervals[i][0])
                newInterval[1] = max(newInterval[1],intervals[i][1])
                print(newInterval[0],newInterval[1])
        res.append(newInterval)
        return res