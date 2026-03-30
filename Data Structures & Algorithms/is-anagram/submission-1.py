class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        container = []
        if len(s)!=len(t):
            return False
        for i in s:
            container.append(i)
        for j in t:
            if j in container:
                container.remove(j)
        if len(container)==0:
            return True
        return False