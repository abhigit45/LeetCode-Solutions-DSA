class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap) > k:
                heapq.heappop(heap)
        res = heapq.heappop(heap)
        return res



        # # Approach 1 using sorting
        # nums.sort()
        # return nums[-k]
        