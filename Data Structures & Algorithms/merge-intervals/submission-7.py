class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
            -------
                --
                ------  -----
                             ------
            - sort intervals
            - res = [intervals[0]]

            for start, end in intervals[1:]
                find end of most recent in res
                if start <= 

                else:
                    res.append([start, end])

            return res
        """
        intervals.sort(key = lambda k: k[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = res[-1][1]

            if start <= lastEnd:
                res[-1][1] = max(end, lastEnd)
            else:
                res.append([start,end])

        return res