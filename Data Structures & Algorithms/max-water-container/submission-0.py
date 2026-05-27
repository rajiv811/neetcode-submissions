class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1

        max_water = 0
        curr_water = 0
        while i < j:
            if heights[i] > heights[j]:
                curr_water = heights[j] * (j-i)
                j-=1
            else:
                curr_water = heights[i] * (j-i)
                i+=1
            max_water = max(max_water,curr_water)
        return max_water

