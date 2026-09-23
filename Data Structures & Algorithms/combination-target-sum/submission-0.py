class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, lst):
            if sum(lst) == target:
                res.append(lst.copy())
                return

            # 2. Loop Through Candidates
            for i in range(start, len(nums)):
                num = nums[i]

                # 3. Constraint Check (Pruning)
                if sum(lst) + num <= target:
                    
                    # 4. Choose: Make the move
                    lst.append(num)

                    # 5. Explore: Recurse with the updated state
                    backtrack(i, lst)

                    # 6. Unchoose: Backtrack / Undo the move
                    lst.pop()

        backtrack(0, [])
        return res