class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_dict, max_char = {}, 0
        res = 0

        l = 0
        for r in range(len(s)):
            count_dict[s[r]] = 1 + count_dict.get(s[r], 0)
            max_char = max(max_char, count_dict[s[r]])

            if (r - l + 1) - max_char > k:
                count_dict[s[l]] -= 1
                l += 1

            res = max(res, (r-l+1))

        return res