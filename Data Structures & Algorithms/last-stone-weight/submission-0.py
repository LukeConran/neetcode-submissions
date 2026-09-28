import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while (len(maxHeap) > 1):
            # print(maxHeap)
            val1 = heapq.heappop(maxHeap)
            val2 = heapq.heappop(maxHeap)

            new_stone = -abs(val1 - val2)
            heapq.heappush(maxHeap, new_stone)  

        return -maxHeap[0]