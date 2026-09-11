import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #if you sort the array, and you do length - h, 
        # can we use the sum of all the piles?
        # the upperbound is k = max(piles), the lower bound is 1
        high = max(piles)
        low = 1
        mid = int((high + low) / 2)
        k=high

        while low <= high:
            count = 0
            print(mid)
            for pile in piles:
                count += math.ceil(pile / mid)
            if count <= h:
                k = mid
                high = mid - 1
                mid = int((high + low) / 2)
            else:
                low = mid + 1
                mid = int((high + low) / 2)

        return k
