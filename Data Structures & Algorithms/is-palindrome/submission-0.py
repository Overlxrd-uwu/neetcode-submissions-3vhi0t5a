class Solution: # 2 pointers
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        l,r= 0,len(newStr)-1
       
        while l<r:
            if newStr[l]==newStr[r]:
                l+=1
                r-=1
            else:
                return False
        return True