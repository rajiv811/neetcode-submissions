class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Brute Force approach
        - visit every possible substring
        o(n) x o(m)

        Sliding Window - 1 pass (o(n))
        hash_map --> Tracks location of characters
        key : char
        val : index
        """

        hash_map = defaultdict(int)
        start_index = 0
        max_ss = 0
        """
        s="aab"
        hash_map = a:0
        max_ss = 1
        hash_map = a:0
        - curr_ss = 0
        """
        for i in range(len(s)):
            if s[i] in hash_map and hash_map[s[i]] >= start_index:
                start_index = hash_map[s[i]] + 1
            hash_map[s[i]] = i
            max_ss = max(i-start_index + 1,max_ss)
        return max_ss