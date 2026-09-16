class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0,0
        res = []

        while i < len(firstList) and j < len(secondList):
            lo = max(firstList[i][0], secondList[j][0])
            high = min(firstList[i][1], secondList[j][1])

            if lo <= high:
                res.append([lo, high])
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return res