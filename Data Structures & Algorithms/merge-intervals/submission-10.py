class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
            -----------
                 -----
                    -------  --------
            res = [interval[0]]

            for start, end in intervals:
                lastEnd = res[-1][1]
                if start <= lastEnd:
                    res[-1][1] = max(lastEnd, end)
                else:
                    res.append([start, end])
            
            return res
        """
        intervals.sort(key = lambda k: k[0])
        res = [intervals[0]]

        for start, end in intervals:
            lastEnd = res[-1][1]

            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)
            else: 
                res.append([start, end])

        return res