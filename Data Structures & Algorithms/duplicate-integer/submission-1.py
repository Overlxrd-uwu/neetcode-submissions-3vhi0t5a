class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        container=[]
        for num in nums:
            if num in container:
                return True
            container.append(num)
        return False
            
        
        
            

            