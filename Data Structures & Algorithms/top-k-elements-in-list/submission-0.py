class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """

        """
        numCount = {}
        res = [[] for i in range(len(nums) + 1)]

        for num in nums:
            numCount[num] = 1 + numCount.get(num, 0)
        
        for num, freq in numCount.items():
            res[freq].append(num)

        final = []

        for i in range(len(res) - 1, 0, -1):
            for item in res[i]:
                final.append(item)
                if len(final) == k:
                    return final
        


        
