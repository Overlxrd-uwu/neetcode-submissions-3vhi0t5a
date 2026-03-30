class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k=len(nums)
        index=[]
        for i in range(k):
            for j in range (i+1,k):
                    if target == nums[i]+nums[j]:
                        index.append(i)
                        index.append(j)
                        return index
            
                

                

