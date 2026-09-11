class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        k = len(numbers) - 1
        while i != k and i-1 != k:
            sum_ = numbers[i] + numbers[k]
            if sum_ == target:
                return [i+1,k+1]
            elif sum_ < target:
                i+=1
            else:
                k-=1