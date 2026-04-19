class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNum = {}

        for n in nums:
            countNum[n] = countNum.get(n, 0) + 1

        heap = []
        for n in countNum.keys():
            heapq.heappush(heap, (countNum[n], n))
            if len(heap) > k:
                heapq.heappop(heap)
            

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res