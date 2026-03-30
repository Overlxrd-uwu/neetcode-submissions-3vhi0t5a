class Solution: # stack + hash mapping
    def isValid(self, s: str) -> bool:
        stack = [] # "(" , "[" , "{"
        closTOopen = { ")":"(", "]":"[","}":"{"  }
        for c in s:
            if c in closTOopen:
                if stack and stack[-1]==closTOopen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False