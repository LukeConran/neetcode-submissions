class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def backtrack(lst):
            if len(lst) == len(nums):
                res.append(lst[:])

            for i in range(len(nums)):
                if not used[i]:
                    lst.append(nums[i])
                    used[i] = True
                    backtrack(lst)
                    used[i] = False
                    lst.pop()

        backtrack([])
        return res