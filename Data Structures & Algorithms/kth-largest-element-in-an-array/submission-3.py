class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Brute Force
        1. Sort in reverse order (nlogn)
        2. return nums[k-1]

        Min Heap removes smallest element
        """
        pq = []
        for n in nums:
            heapq.heappush(pq,n)
            if len(pq) > k:
                heapq.heappop(pq)
        return pq[0]