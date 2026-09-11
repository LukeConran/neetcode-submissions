class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(heights) - 1

        while i != j and i - 1 != j:
            curr_area = min(heights[i], heights[j]) * (j-i)
            print(curr_area)
            if curr_area > max_area:
                max_area = curr_area
            
            if heights[i] > heights[j]:
                j -= 1
            elif heights[i] < heights[j]:
                i += 1
            else:
                i += 1
                j -= 1
        
        return max_area