class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            sorted_ascii = tuple(sorted([ord(char) for char in s]))
            if(sorted_ascii in d):
                d[sorted_ascii].append(s)
            else:
                d[sorted_ascii] = [s]
        return list(d.values())