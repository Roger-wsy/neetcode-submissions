class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for n in stones:
            maxHeap.append(-n)
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)
            if x < y:
                heapq.heappush(maxHeap, -(y-x))
            elif x > y:
                heapq.heappush(maxHeap, -(x-y))
        
        return -maxHeap[0] if maxHeap else 0