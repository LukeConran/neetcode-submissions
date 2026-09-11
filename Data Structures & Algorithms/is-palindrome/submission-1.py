class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join([char for char in s.lower() if char.isalnum()])
        print(new_s)

        i = 0
        k = len(new_s) - 1
        while i != k and i-1 != k:
            if new_s[i] != new_s[k]:
                return False
            i += 1
            k -= 1
        return True
        