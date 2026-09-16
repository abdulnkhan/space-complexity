class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        numCount = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            numCount[num] = 1 + numCount.get(num, 0)

        for n, f in numCount.items():
            freq[f].append(n)

        for i in range(len(freq)-1, 0, -1):
            for r in freq[i]:
                res.append(r)

                if len(res) >= k:
                    return res