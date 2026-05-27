"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        Variables
        intervals - meeting i with [start,end]
        Return
        Min # of days required to schedule all meetings

        Visualization
        intervals = [(0,40),(5,10),(15,20)]

        x ------------------x
           x---x
                      x----x

         1.  2.   1.     2. 1. 0 

         The overlaps tell us the number of days we need to
         schedule the meeting. In the case, we take the MAX.
         Which is 2.

         1. Create two sorted intervals
         start = [0,5,15]
         end = [10,20,40]
         0 -> 10 + 1
         5 -> 10 + 1
         15 -> 10 -1
         15 -> 20 + 1
         [] -> 30 0
        """
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        i = 0
        j = 0
        count = 0
        max_count = 0
        while i < len(start):
            if start[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            max_count = max(max_count,count)
        return max_count