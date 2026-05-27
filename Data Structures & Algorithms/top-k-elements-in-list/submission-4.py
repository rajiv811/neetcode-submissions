class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Key: number, Value: frequency
        count = collections.defaultdict(int)
        for num in nums:
            count[num] += 1
        """
        1:1
        2:2
        3:3
        """
        frequency = [[] for i in range(len(nums)+1)]
        for n,c in count.items():
            frequency[c].append(n)
        """
        [[],[1],[2],[3],[],[]...]
        """
        res = []
        for j in range(len(frequency)-1,0,-1):
            for n in frequency[j]:
                res.append(n)
                if len(res) == k:
                    return res

            
