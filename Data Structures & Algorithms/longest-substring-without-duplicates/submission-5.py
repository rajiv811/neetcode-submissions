class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1. Use dictionary to store character and index within a window
        # d = {'a':0, 'b':1, 'c':2}
        # 2. if max(d.keys > 1, update window to position of 1st char+1)

        """
        zxyz
        z
        d = {z:0} .. d = {z:0,x:1,y:2}
        2nd z and l = 3:

        """
        l = 0
        d = {}
        max_string = 0
        for r in range(len(s)):
            if s[r] in d and d[s[r]] >= l:
                l = d[s[r]]+1
            d[s[r]] = r
            max_string = max(max_string,r-l+1)
        
        return max_string
