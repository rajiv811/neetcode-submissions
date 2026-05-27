class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # [2,2,3,4,6]
        # [2,2,3,2] -> [2,2,2,3]
        # [2,2,1] -> [1,2,2]
        # [1,0] -> [0,1]
        # [1]

        # [-3,-7,-2] -> [-7,-3,-2]
        # [-4,-2]
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first < second:
                new_stone = first - second
            else:
                new_stone = second - first
            
            heapq.heappush(stones, new_stone)
        
        if not stones:
            return 0
        return abs(stones[0])
            
