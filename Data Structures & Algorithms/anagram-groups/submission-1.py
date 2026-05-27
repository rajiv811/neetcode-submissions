class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        ["act","cat","bat"] --> ["act","act","abt"] -->
        {
            ('a','c','t'): ["act","cat"],
            "abt": ["bat]
        }
        """
        hash_map = defaultdict(list)

        for word in strs:
            sorted_word = tuple(sorted(word))
            hash_map[sorted_word].append(word)
        
        res = []
        for l in hash_map.values():
            res.append(l)
        return res
