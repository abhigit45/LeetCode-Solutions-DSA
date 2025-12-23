class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        #Using BruteForce
        n = len(nums)
        while n > 1:
            curr = []
            for i in range(n-1):
                val = (nums[i] + nums[i+1]) % 10
                curr.append(val)
            nums = curr
            n-=1
        res = nums[0]
        return res
        
     


        # #Using Binomial Coefficient
        # n = len(nums)
        # coeff = 1  
        # result = 0

        # for i in range(n):
        #     result = (result + coeff * nums[i]) % 10
        #     # for next i (C(n-1, i+1))
        #     coeff = coeff * (n - 1 - i) // (i + 1)

        # return result
