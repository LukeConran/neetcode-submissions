import math, heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # print(points)
        minHeap = [self.Eucl(point[0], point[1], 0, 0) for point in points]
        together = [(minHeap[i], points[i]) for i in range(len(points))]
        # print(together)

        heapq.heapify(together)
        # print(together)

        res = [heapq.heappop(together)[1] for i in range(k)]
        # print(res)
        return res


    def Eucl(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)