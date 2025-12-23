class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4, -1, -1, 0, 1, 2]
        res = []
        sorted_array = sorted(nums)
        for i in range(len(sorted_array) - 2):
            if i > 0 and sorted_array[i] == sorted_array[i - 1]:
                continue

            left = i + 1
            right = len(sorted_array) - 1
        
            while left< right:
                total = sorted_array[i] + sorted_array[left] + sorted_array[right]
                if total == 0:
                    res.append([sorted_array[i],sorted_array[left],sorted_array[right]])
                    left += 1
                    right -= 1
                    while left < right and sorted_array[left] == sorted_array[left - 1]:
                        left += 1

                    while left < right and sorted_array[right] == sorted_array[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return res



        