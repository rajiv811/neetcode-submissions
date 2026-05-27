class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        print(j)
        max_area = 0
        while i < j:
            curr_area = (j-i) * min(heights[i],heights[j])
            max_area = max(curr_area,max_area)
            if heights[i] > heights[j]:
                j-=1
            elif heights[j] >= heights[i]:
                i+=1
        
        return max_area
