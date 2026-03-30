class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s = min(nums)
        max_box = max(nums)
        box = {i: 0 for i in range(s, max_box + 1)}

        for num in nums:
            box[num] = 1   # just mark it exists

        longest = 0
        current = 0

        for i in range(s, max_box + 1):
            if box[i] > 0:
                current += 1
                longest = max(longest, current)
            else:
                current = 0

        return longest
        
        