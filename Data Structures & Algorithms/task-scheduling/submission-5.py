class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        To populate maxHeap we will have a freqDict
        maxHeap with deque
        we're going to pop for maxHeap -> add entry to deque with the cnt and time we can execute it
        """
        freqDict = {}
        for t in tasks:
            freqDict[t] = 1 + freqDict.get(t, 0)

        maxHeap = [-cnt for cnt in freqDict.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while q or maxHeap:
            time += 1
            if maxHeap:
                taskCount = heapq.heappop(maxHeap)
                taskCount += 1
                if taskCount:
                    q.append([taskCount, time + n])

            if q and q[0][1] == time:
                taskCount, _ = q.popleft()
                heapq.heappush(maxHeap, taskCount)

        return time


