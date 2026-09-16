class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        res = []
        for num in nums:
            numCount[num] = 1 + numCount.get(num, 0)

        buc = [[] for i in range(len(nums) + 1)]

        for num, freq in numCount.items():
            buc[freq].append(num)

        # [[1], [2], [3]]

        for j in range(len(buc) - 1, 0, -1):
            for m in buc[j]:
                res.append(m)

                if len(res) >= k:
                    return res