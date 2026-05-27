class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Variables
        intervals - list of lists, where interval[i] consists of a start and end
        newInterval - list that we want to insert

        Problem
        Insert newInterval, such that intervals is STILL in
        ascending order.
        If newInterval overlaps with intervals, merge interval such that
        overlap no longer exists.

        Questions
        Is intervals sorted? Yes
        Can interval be negative? No

        Return
        Return intervals with newInterval either merged in, or in order

        Examples
        Case 1 - Merge the interval
        Input: intervals = [[1,3],[4,6],[8,9]], newInterval = [2,10]
        newInterval = [1,10]
        newInterval = [1,10]
        newInterval = [1,10]

        Case 2 - No overlap
        intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]
        """
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]
        res.append(newInterval)
        return res
