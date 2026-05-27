class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            heapq.heappush(h,-n)
        
        for i in range(k-1):
            heapq.heappop(h)
        
        return -(h[0])