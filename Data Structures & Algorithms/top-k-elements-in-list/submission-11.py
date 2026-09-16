class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        freqArr = [[] for i in range(len(nums) + 1)]
        res = []
        for num in nums:
            numCount[num] = 1 + numCount.get(num, 0)

        for n, freq in numCount.items():
            freqArr[freq].append(n)

        for j in range(len(freqArr)-1, 0, -1):
            for m in freqArr[j]:
                if len(res) < k:
                    res.append(m)

        return res
        