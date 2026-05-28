class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # dict to store the index of the characters

        hash_map = {}

        l = 0
        longest_ss = 0
        """
        dvdf
        {
        d: 0
        v: 1
        
        }
        """
        for r in range(len(s)):
            if s[r] in hash_map and hash_map[s[r]] >= l:
                l = hash_map[s[r]] + 1
            hash_map[s[r]] = r
            longest_ss = max(longest_ss, r-l + 1)
        
        return longest_ss


