class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        for i in range(len(s)):
            count_s[s[i]] = 1+count_s.get(s[i],0)
        for j in range(len(t)):
            if t[j] not in count_s:
                return False
            if count_s[t[j]] == 0:
                return False
            count_s[t[j]] -= 1
        for n,c in count_s.items():
            if c > 0:
                return False
        return True
        