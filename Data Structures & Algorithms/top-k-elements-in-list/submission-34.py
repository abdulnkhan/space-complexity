class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}

        for n in nums:
            freqDict[n] = 1 + freqDict.get(n, 0)

        heap = []
        res = []

        for n in freqDict:
            heapq.heappush(heap, [freqDict[n], n])

            if len(heap) > k:
                heapq.heappop(heap)

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res