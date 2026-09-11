class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        total = 1
        zero_loc = set()
        has_zero = False
        
        for i in range(len(nums)):
            if nums[i] == 0:
                has_zero = True
                zero_loc.add(i)
            else: total *= nums[i]

        print(zero_loc)
        for i in range(len(output)):
            if has_zero:
                output[i] = total if (i in zero_loc and len(zero_loc) == 1) else 0
            else: output[i] = int(total / nums[i])

        return output