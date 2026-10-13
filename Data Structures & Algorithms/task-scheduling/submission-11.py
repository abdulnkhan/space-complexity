class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        freqDict = {"A": 2, "B": 3}
        maxHeap 
        heapify
        q = deque()

        while maxHeap or q:

        """

        freqDict = {}
        for t in tasks:
            freqDict[t] = 1 + freqDict.get(t, 0)

        maxHeap = [-i for i in freqDict.values()]
        heapq.heapify(maxHeap)
        q = deque()
        t = 0

        while maxHeap or q:
            t += 1
            if maxHeap:
                taskCnt = heapq.heappop(maxHeap)
                taskCnt += 1
                if taskCnt:
                    q.append([taskCnt, t + n])

            if q and q[0][1] == t:
                taskCnt, _ = q.popleft()
                heapq.heappush(maxHeap, taskCnt)

        return t
