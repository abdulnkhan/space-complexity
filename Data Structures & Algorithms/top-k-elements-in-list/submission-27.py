class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
            {}

            []
        """
        numMap = {}
        for n in nums:
            numMap[n] = 1 + numMap.get(n, 0)

        # {3: 2}

        freqArr = [[] for i in range(len(nums)+1)]
        for num, freq in numMap.items():
            freqArr[freq].append(num)

        m = 0
        res = []
        for num in reversed(freqArr):
            for n in num:
                res.append(n)
                m += 1
                if m >= k:
                    return res