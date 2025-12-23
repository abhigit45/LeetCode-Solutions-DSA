class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
            else:
                res.append(num)
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
                break
        return res

        # dup = -1
        # missing = 0
        # for i in range(len(nums)):
        #     if nums[abs(nums[i])-1] < 0:
        #         dup = abs(nums[i])
        #     else:
        #         nums[abs(nums[i])-1] *= -1
        # # return nums
        # for i in range(len(nums)):
        #     if nums[i] > 0 :
        #         missing = i + 1
        # return [dup,missing]


