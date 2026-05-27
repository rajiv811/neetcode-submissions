class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        print(sorted(tuple(s1)))

        sorted_tuple_val = sorted(tuple(s1))
        l = 0
        for r in range(len(s1)-1,len(s2)):
            curr_window_val = s2[l:r+1]
            print(curr_window_val)
            if sorted_tuple_val == sorted(tuple(curr_window_val)):
                return True
            l += 1
        return False



        