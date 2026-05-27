class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #use dictionary
        #sliding window
        d = {}
        l = 0
        max_count = 0

        for r in range(len(s)):
            if s[r] in d and d[s[r]] >= l:
                l = d[s[r]]+1
            d[s[r]] = r
            max_count = max(max_count,r-l+1)
        
        return max_count





        