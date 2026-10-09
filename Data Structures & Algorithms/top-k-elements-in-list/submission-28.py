class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # Freq Map # {1: 4, ...}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        heap = []
        for n in count:
            heapq.heappush(heap, (count[n], n)) # (freq, num)

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res