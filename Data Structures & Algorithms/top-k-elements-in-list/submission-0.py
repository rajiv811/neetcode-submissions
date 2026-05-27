class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a dictionary to keep track of the count
        #create a bucket array such that it is as long as the largest number
            #each index represents the number, and value represents the frequency
        
        #key = num, val = freq
        count = {}

        # i is the freqency, the array val at i is the numbers with that frequency
        freq = [[] for i in range(len(nums)+1)]

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i],0)
        for n,c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
