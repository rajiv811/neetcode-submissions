class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # "AABCDBC", k = 2
        # Window - max(d.values()) > k --> increment the window, update left pointer
        # Window - max(d.values()) < k --> update curr_lrc, increment r
        d = defaultdict(int)
        """
        X:1, window = 1, max(d.values()) = 1, max_lrc = 1
        X:1|Y:1, window = 2, max = 1, max_lrc = 2
        X:1|Y:2 window = 3, max = 2, max_lrc = 3
        X:2|Y:2 window = 4, max = 2, max_lrc = 4
        """
        l = 0
        max_lrc = 0
        for r in range(len(s)):
            d[s[r]] += 1
            window = (r - l) + 1
            if window - max(d.values()) > k:
                d[s[l]] -= 1
                l += 1
            else:
                curr_lrc = (r-l)+1
                max_lrc = max(max_lrc,curr_lrc)
        return max_lrc