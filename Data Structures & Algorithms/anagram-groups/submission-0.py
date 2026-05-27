class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        #key = sorted str
        # val = actual word
        for i in range(len(strs)):
            sorted_key = tuple(sorted(strs[i]))
            if sorted_key not in d:
                d[sorted_key] = [strs[i]]
            else:
                d[sorted_key].append(strs[i])
        return d.values()