class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        if sorted(s)==sorted(t):
            return True
        else: 
            return False"""
        """
        dic  = {}
        for c in s:
            dic[c]= dic.get(c,0)+1
        for c in t:
            dic[c]= dic.get(c,0)-1
        for val in dic.values():
            if val!=0:
                return False
        return True"""
        n = [0] * 26 
        for item in s:
            n[ord(item)-ord('a')]+=1
        for item in t:
            n[ord(item)-ord('a')]-=1
        for num in n:
            if num!=0:
                return False
        return True