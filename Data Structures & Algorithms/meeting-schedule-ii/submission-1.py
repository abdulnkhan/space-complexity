"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
            Brute Force: 
            total_rooms = 1
            sort(key = intervals[0])
            for i in range(len(intervals))
                start, end = intervals[i][0], intervals[i][1]
                for j in intervals[i+1:]:
                    s_2, e_2 = intervals[j][0], intervals[j][1]
                    if s_2 < start:
                        total_rooms += 1
            
            return total_rooms

        """

        s = sorted([i.start for i in intervals])
        e = sorted([i.end for i in intervals])

        res, count = 0, 0
        lp = rp = 0

        while lp < len(intervals):
            if s[lp] < e[rp]:
                lp += 1
                count += 1
            else:
                rp += 1
                count -= 1

            res = max(res, count)

        return res

