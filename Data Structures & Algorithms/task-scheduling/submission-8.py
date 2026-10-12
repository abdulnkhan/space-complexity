class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqDict = {}
        for t in tasks:
            freqDict[t] = 1 + freqDict.get(t, 0)

        maxHeap = [-i for i in freqDict.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                taskCnt = heapq.heappop(maxHeap)
                taskCnt += 1
                if taskCnt != 0:
                    q.append([taskCnt, time + n])

            if q and q[0][1] == time:
                taskCnt, _ = q.popleft()
                heapq.heappush(maxHeap, taskCnt)

        return time