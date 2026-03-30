class Solution: # brutal force
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        length = len(nums)

        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        res.add(tuple(triplet))

        return [list(x) for x in res]