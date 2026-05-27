class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        for x,y in points:
            distance = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(h,[distance,[x,y]])
        
        res = []
        while k > 0:
            dist,cord = heapq.heappop(h)
            res.append(cord)
            k -= 1 
        
        return res