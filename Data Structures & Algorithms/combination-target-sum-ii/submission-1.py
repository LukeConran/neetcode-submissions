class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        
        def backtrack(start, lst, remaining):
            if remaining == 0:
                res.append(lst[:])
                return
                
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                    
                num = candidates[i]
                
                if num > remaining:
                    break
                    
                lst.append(num)
                backtrack(i + 1, lst, remaining - num)
                lst.pop()

        backtrack(0, [], target)
        return res