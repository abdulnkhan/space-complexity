class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
            first create dict {num:freq}
            then create array where index is freq and the items are actual numbers
            then iterate backwards from array and print numbers
        """
        numCount = {}
        freqArr = [[] for i in range(len(nums) + 1)]
        res = []
        for num in nums:
            numCount[num] = 1 + numCount.get(num, 0)

        for i, f in numCount.items():
            freqArr[f].append(i)

        for i in range(len(freqArr)-1,0,-1):
            for j in freqArr[i]:
                res.append(j)

                if len(res) == k:
                    return res