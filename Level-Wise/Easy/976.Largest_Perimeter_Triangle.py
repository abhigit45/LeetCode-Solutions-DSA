class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        #greedy Search
        nums.sort()
        n = len(nums)
        for i in range(n-1,1,-1):
            if nums[i-1] + nums[i-2] > nums[i]:
                curr_sum = nums[i-1] + nums[i-2] + nums[i]
                return curr_sum
        return 0




        # #Brute force 
        # n = len(nums)
        # max_len = 0
        # nums.sort()
        # for i in range(n-1,1,-1):
        #     left , right = 0 , i- 1
        #     while left < right:
        #         if nums[left] + nums[right] > nums[i]:
        #             curr_sum = nums[left] + nums[right] + nums[i]
        #             if curr_sum > max_len:
        #                 max_len = curr_sum
        #             right -= 1
        #         else:
        #             left += 1
        # if max_len == 0:
        #     return 0
        # else:
        #     return max_len


        