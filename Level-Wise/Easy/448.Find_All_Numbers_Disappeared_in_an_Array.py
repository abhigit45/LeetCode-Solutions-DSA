class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # O(1) space
        res = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        for i in range(len(nums)):
            if nums[i] < 0:
                continue
            else:
                res.append(i+1)
        return res


        # nums_set = set(nums)
        # n = len(nums)
        # res = []
        # for i in range(1,n+1):
        #     if i in nums_set:
        #         continue
        #     else:
        #         res.append(i)
        # return res

        