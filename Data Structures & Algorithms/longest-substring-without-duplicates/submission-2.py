class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        answer = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            answer = max(answer, r - l + 1)

        return answer
        # This one is definitely difficult for me. Essentially, as we move through the string,
        # we add the current character to a set, unless it is already in the set. If it is in the
        # the set, we remove from the set until that specific character is gone, and then add it
        # back so there are no longer duplicates in the window we see
