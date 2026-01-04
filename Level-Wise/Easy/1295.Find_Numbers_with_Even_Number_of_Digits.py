class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # Without type Conversion
        count = 0
        for num in nums:
            digit = 0
            while num > 0:
                num //= 10
                digit += 1
            if digit % 2 == 0:
                count += 1
        return count

        # Using Type Conversion
        # count = 0
        # for num in nums:
        #     if len(str(num)) % 2 == 0:
        #         count += 1
        # return count

        