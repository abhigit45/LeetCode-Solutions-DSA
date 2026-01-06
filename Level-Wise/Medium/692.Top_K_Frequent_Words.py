class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        heap = []
        for word,count in freq.items():
            heapq.heappush(heap,(-count,word))
            # if len(heap) > k:          #This works only for minHeap
            #     heapq.heappop(heap)
        res = []
        while heap:
            num = heapq.heappop(heap)[1]
            res.append(num)
            if len(res) == k:
                break
        
        return res
        
        
        