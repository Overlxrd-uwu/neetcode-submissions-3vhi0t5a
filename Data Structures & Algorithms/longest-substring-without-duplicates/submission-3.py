class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        box = set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in box:
                box.remove(s[l])
                l+=1
            box.add(s[r])
            res = max(res,r-l+1)
        return res

            