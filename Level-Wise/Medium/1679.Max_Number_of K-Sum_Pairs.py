class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #Using HAshmap
        freq = {}
        op = 0
        n = len(nums)
        for num in nums:
            complement = k - num
            if complement in freq and freq[complement] > 0:
                freq[complement] -= 1
                op += 1
            else:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1
        return op






        #Using Two Pointer
        # left = 0
        # right = len(nums) - 1
        # op = 0
        # nums.sort()
        # while left < right:
        #     summ = nums[left] + nums[right]
        #     if k == summ:
        #         left += 1
        #         right -= 1
        #         op += 1
        #     else:
        #         if summ < k:
        #             left += 1
        #         else:
        #             right -= 1
                
                
        # return op


        