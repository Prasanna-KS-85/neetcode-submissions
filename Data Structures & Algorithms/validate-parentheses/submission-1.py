class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashset = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }

        for c in s:
            if c in hashset:
                if stack and stack[-1] == hashset[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else  False 
        