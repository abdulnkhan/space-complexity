class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Initializing minHeap
        self.minHeap = nums
        self.k = k

        # Creating the heap
        heapq.heapify(self.minHeap)

        #Popping elements initially since minHeap needs to be length k and then we
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Push to the heap anyways
        heapq.heappush(self.minHeap, val)
        
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
            
        return self.minHeap[0]
