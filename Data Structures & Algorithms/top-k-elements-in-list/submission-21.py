class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}

        for num in nums:
            numCount[num] = 1 + numCount.get(num, 0)

        freqArr = [[] for i in range(len(nums) + 1)]

        for num, freq in numCount.items():
            freqArr[freq].append(num)

        res = []
        
        for i in range(len(freqArr)-1,0,-1):
            for j in freqArr[i]:
                res.append(j)

                if len(res) == k:
                    return res
