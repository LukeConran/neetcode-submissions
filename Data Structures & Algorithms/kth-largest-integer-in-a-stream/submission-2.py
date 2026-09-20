class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []
        for num in nums:
            if len(self.minHeap) < k:
                heapq.heappush(self.minHeap, num)
            else:
                if num > self.minHeap[0]:
                    heapq.heappop(self.minHeap)
                    heapq.heappush(self.minHeap, num)

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
                heapq.heappush(self.minHeap, val)
        else:
            if val > self.minHeap[0]:
                heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, val)
        return self.minHeap[0]
        
