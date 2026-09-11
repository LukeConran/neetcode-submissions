class Solution:
    def trap(self, height: List[int]) -> int:
        arr_left_maxes = [0] * len(height)
        arr_right_maxes = [0] * len(height)
        
        for i in range(len(height)):
            if i == 0:
                arr_left_maxes[i] = height[i]
                curr_max = height[i]
                continue
            
            arr_left_maxes[i] = curr_max
            curr_max = max(height[i], curr_max)

        rev_height = height[::-1]
        for i in range(len(rev_height)):
            if i == 0:
                arr_right_maxes[i] = rev_height[i]
                curr_max = rev_height[i]
                continue
            
            arr_right_maxes[i] = curr_max
            curr_max = max(rev_height[i], curr_max)
        arr_right_maxes = arr_right_maxes[::-1]

        # print(arr_left_maxes)
        # print(arr_right_maxes)
        # print(height)

        total_water = 0
        for i in range(1, len(height) - 1):
            other = min(arr_right_maxes[i], max(arr_left_maxes[i] - height[i], 0))
            total_water += min(other, min(arr_left_maxes[i], max(arr_right_maxes[i] - height[i], 0)))
            # print(f"i={i}, total_water={total_water}")

        return total_water