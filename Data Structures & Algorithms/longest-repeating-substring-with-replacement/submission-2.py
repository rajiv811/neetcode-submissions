class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = collections.Counter()
        max_substring = 0
        l = 0
        for r in range(len(s)):
            d[s[r]] += 1
            window = (r-l)+1
            if window - max(d.values()) > k:
                d[s[l]] -= 1
                l += 1
            max_substring = max(max_substring,r-l+1)
        return max_substring

