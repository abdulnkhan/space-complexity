class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        numCount = {}
        freq = [[] for v in range(len(nums) + 1)]

        for i in nums:
            numCount[i] = 1 + numCount.get(i, 0)
            
        for j, l in numCount.items():
            freq[l].append(j)

        for m in range(len(freq)-1, 0, -1):
            for r in freq[m]:
                if len(res) < k:
                    res.append(r)
        return res