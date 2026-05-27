class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        create a hashmap
        f_word = {
            'r': 2,
            'a': 2,
            'e': 1,
            'c': 2,
        }

        For second word, we can subtract from existing hashmap. If val
        drops below 0, return False. If char not in f_word, return False
        If there are remaining values in f_word (non 0 and non negative), return
        False
        """
        if len(s) != len(t):
            return False
        f_word = defaultdict(int)
        for char in s:
            f_word[char] += 1
        
        for char in t:
            if char not in f_word:
                return False
            if f_word[char] == 0:
                return False
            f_word[char] -= 1
        return True