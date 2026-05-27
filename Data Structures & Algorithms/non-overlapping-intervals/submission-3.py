class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Is the input array sorted?
        No

        Return
        Minimum number of intervals to remove so that there are
        no overlapping intervals

        Example
        sorted_intervals = [[0,20],[1,4],[5,6]]

        Algorithm
        When we come across an overlap, pop the value that takes
        up the greatest space. compare prev[1] and curr[1].
        Type of greedy solution, we pick optimal solution at 
        each overlap

        Edge Cases:
        len == 0 -> return 0
        len == 1 -> return 0

        sorted_intervals = [[0,20],[1,4],[5,6]]
        prev = [0,20] curr = [1,4]
        prev = [1,4] curr = [5,6]
        """
        if len(intervals) <= 1:
            return 0

        count = 0
        sorted_intervals = sorted(intervals,key=lambda x: x[0])
        prev = sorted_intervals[0]

        for curr in sorted_intervals[1:]:
            # If overlap
            if prev[1] > curr[0]:
                count += 1
                if prev[1] > curr[1]:
                    prev = curr
            else:
                prev = curr

        return count