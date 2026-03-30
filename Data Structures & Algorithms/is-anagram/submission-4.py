class Solution: # hash count
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return False
        dic={}
        for i in s:
            dic[i]=dic.get(i,0)+1
        for j in t:
            dic[j]=dic.get(j,0)-1
        for item in dic.values():
            if item!=0:
                return False
        return True