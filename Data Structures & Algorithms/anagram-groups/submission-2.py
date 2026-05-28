class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for s in strs:
            sorted_tuple = tuple(sorted(s))
            hash_map[sorted_tuple].append(s)
        
        res = []
        for k,v in hash_map.items():
            res.append(v)
        return res