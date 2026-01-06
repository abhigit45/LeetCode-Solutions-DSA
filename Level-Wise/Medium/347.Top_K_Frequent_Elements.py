class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        heap = []
        for num,count in freq.items():
            heapq.heappush(heap,(count,num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            a = heapq.heappop(heap)[1]
            res.append(a)
        res.reverse()
        return res



        