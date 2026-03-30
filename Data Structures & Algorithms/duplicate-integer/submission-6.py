class Solution: # that hashset remove dup so if setlen < origin (no dup)
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)