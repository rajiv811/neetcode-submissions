class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Brute Force
        """
        res = [0] * len(temperatures)
        # res [0,0,0,0,0,0,0]
        for i in range(len(temperatures)):
            count = 0
            for j in range(i+1,len(temperatures)):
                if temperatures[i] >= temperatures[j]:
                    count += 1
                else:
                    count += 1
                    res[i] = count
                    break
        return res