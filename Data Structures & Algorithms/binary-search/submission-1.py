class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = int(high/2)
        if target < nums[low] or target > nums[high]:
            return -1
            
        while nums[mid] != target:
            if high == low:
                return -1
            elif target > nums[mid]:
                low = mid + 1
                mid = int((high + low) / 2)
            else:
                high = mid - 1
                mid = int((high + low) / 2)
        
        return mid