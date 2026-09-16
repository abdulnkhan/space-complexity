class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
            count = {}
            freq = [[] for i in len(nums)+1]
            go backwards in freq array and popleft
        """
        numCount = {}
        freqA = [[] for i in range(len(nums)+1)]

        for num in nums:
            numCount[num] = 1 + numCount.get(num,0)
        
        for num, freq in numCount.items():
            freqA[freq].append(num)

        res = []
        for i in range(len(freqA)-1,0,-1):
                for m in freqA[i]:    
                    res.append(m)
                    if len(res) == k:
                        return res