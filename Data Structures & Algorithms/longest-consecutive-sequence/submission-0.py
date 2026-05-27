class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Cannot sort as sorting is O(n log n)
        hash_set = set()
        for i in range(len(nums)):
            hash_set.add(nums[i])
        longest_seq = 0
        curr_seq = 0
        for i in range(len(nums)):
            if (nums[i] - 1) not in hash_set:
                # We know that this is the first number in the sequence
                curr_seq = 1
                count = 1
                while (nums[i] + count) in hash_set:
                    curr_seq += 1
                    count += 1

            longest_seq = max(longest_seq,curr_seq)
        return longest_seq

