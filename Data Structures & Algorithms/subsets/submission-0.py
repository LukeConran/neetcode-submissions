import itertools

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for i in range(1, len(nums) + 1):
            res.extend(itertools.combinations(nums, i))

        return [list(x) for x in res]