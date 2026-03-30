class Solution: # hash
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k most freq
        dic = {}
        
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        arr = []
        for key, val in dic.items():
            arr.append((val, key))   # (frequency, number)
        
        arr.sort(reverse=True)   # sort by frequency
        res = []
        
        for i in range(k):
            res.append(arr[i][1])    # take number, not frequency
        
        return res