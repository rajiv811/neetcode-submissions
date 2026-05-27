class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # count dictionary
        # key: num, val: freq

        count = {}

        #freq list
        # index: freqency, list associated with index: nums with that freqency

        freq = [[] for i in range(len(nums)+1)]

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i],0)
        for n,c in count.items():
            freq[c].append(n)
        
        res = []
        for j in range(len(freq)-1,0,-1):
            for n in freq[j]:
                res.append(n)
                if len(res) == k:
                    return res
        
