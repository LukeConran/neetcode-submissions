class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        u = [ord(char) for char in s]
        v = [ord(char) for char in t]
        u = sorted(u)
        v = sorted(v)
        return u == v