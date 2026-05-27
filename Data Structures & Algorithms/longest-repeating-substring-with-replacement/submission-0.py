class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = collections.Counter()
        longest_ss = 0
        curr_ss = 0
        l = 0
        # A A B B B A
        for r in range(len(s)):
            d[s[r]] += 1
            window = r - l + 1
            if window - max(d.values()) <= k:
                curr_ss = r - l + 1
            else:
                d[s[l]] -= 1
                l += 1
                curr_ss = r-l+1
            longest_ss = max(longest_ss,curr_ss)
        return longest_ss
