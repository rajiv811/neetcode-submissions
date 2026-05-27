class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Algorithm
        # 1. read s1 and s2[:k] into a dictionary
        # 2. iterate through s2 0->(len-k)
            # a. delete prev element (or counter -= 1)
            # b. add next element (i+k)

        k = len(s1)
        d1 = collections.Counter(s1)
        d2 = collections.Counter(s2[:k])

        if d1 == d2:
            return True
        
        for i in range(len(s2)-k):
            # a
            if d2[s2[i]] == 1:
                del d2[s2[i]]
            elif d2[s2[i]] > 1:
                d2[s2[i]] -= 1

            # b

            if s2[i+k] in d2:
                d2[s2[i+k]] += 1
            else:
                d2[s2[i+k]] = 1
            
            if d1 == d2:
                return True
        
        return False
        
                
            
            