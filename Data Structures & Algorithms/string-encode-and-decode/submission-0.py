class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        2 things we need to encode with:
        1. Delimiter - something that indicates that we've moved onto next word
        2. Length of the string
        """
        res = ""
        for s in strs:
            new_s = str(len(s)) + "#" + s
            res += (new_s)
        return res
    def decode(self, s: str) -> List[str]:
            res = []
            i = 0
            while i < len(s):
                j = i
                while s[j] != "#":
                    j+=1
                length = int(s[i:j])
                i = j + 1
                j = i + length
                res.append(s[i:j])
                i = j
            return res
