class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        di={}
        for num in nums:
            di[num]=di.get(num,0)+1
        for val in di.values():
            if val>1:
                return True
        return False