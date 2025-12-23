class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        #Two pointer Approach

        count = 0
        n = len(nums)
        if n< 3:
            return 0
        nums.sort()
        for i in range(n-1,1,-1):
            left , right = 0 , i -1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count

        #### Brute Force Aprroach
        # count = 0
        # n = len(nums)
        # for i in range(n - 2):
        #     for j in range(i+1, n-1):
        #         for k in range(j+1, n):
        #             if nums[i] + nums[j] > nums[k]:
        #                 count += 1
        # return count
        