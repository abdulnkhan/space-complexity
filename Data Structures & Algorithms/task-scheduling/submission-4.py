class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        I'm going to use a maxHeap in conjunction with a queue
        freqDict = {"A":2, "B":1, ...}
        maxHeap = [-cnt for cnt in freqDict.values()]
        q = deque()

        while q or maxHeap:
        """
        freqDict = {}

        for t in tasks:
            freqDict[t] = 1 + freqDict.get(t, 0)

        maxHeap = [-cnt for cnt in freqDict.values()]
        heapq.heapify(maxHeap) # [t1_cnt, t2_cnt ...]
        q = deque() # [[taskCnt, time]]
        time = 0

        while maxHeap or q:
            time += 1
         
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0: 
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                taskCnt, _ = q.popleft()
                heapq.heappush(maxHeap, taskCnt)

        return time


