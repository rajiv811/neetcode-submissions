class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Case 1: New Interval is less than the interval we are looking at
            # In that case, we add newInterval to res, and then return res = res + interval[i:]
            #  new interval = [1,3] i interval = [4,5]
        # Case 2: New Interval is > than intervals[i], append intervals[i] to res
        # Case 3: Over lap
        # ne: [2,5] i = [0,1] [2,7] [9,12] 
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0],intervals[i][0]),
                    max(newInterval[1],intervals[i][1])
                ]
        res.append(newInterval)
        return res