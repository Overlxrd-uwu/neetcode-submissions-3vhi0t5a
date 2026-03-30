class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        if sorted(s)==sorted(t):
            return True
        else: 
            return False"""
        
        dic  = {}
        for c in s:
            dic[c]= dic.get(c,0)+1
        for c in t:
            dic[c]= dic.get(c,0)-1
        for val in dic.values():
            if val!=0:
                return False
        return True
        