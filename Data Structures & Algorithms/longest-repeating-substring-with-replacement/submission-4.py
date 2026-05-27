class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = collections.Counter()
        max_length = 0
        l = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            window = r-l+1
            print(window)
            print(freq)
            if abs(max(freq.values())-window) <= k:
                max_length = max(max_length,window)
            else:
                freq[s[l]] -= 1
                l += 1
        return max_length

