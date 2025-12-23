class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 24 12 4 1 right all
        # 1 1 2 6 left all
        n = len(nums)
        output = [1] * n

        left = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]

        right = 1
        for i in range(n-1,-1,-1):
            output[i] *= right
            right *= nums[i]
        return output
            



      

        

        