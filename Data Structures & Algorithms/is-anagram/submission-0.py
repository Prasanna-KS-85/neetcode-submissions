class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length1 = len(s)
        length2 = len(t)
        if length1 != length2:
            return False
        return sorted(s) == sorted(t)
        