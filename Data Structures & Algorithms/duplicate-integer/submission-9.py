class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(set(nums))<len(nums) hash set
        """
            dic = {}
            for item in nums:
                dic[item]=dic.get(item,0)+1
            for key,val in dic.items():
                if val>1:
                    return True
            return False """
        # brutal 
        for  i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False


