class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        def is_sorted_ascending(arr):
            """Checks if a list is sorted in ascending order."""
            return arr == sorted(arr)

        def minPairSum(nums):
            min_pair = float('inf')
            min_pair_index = 0
          
            for i in range(len(nums)-1):
                curr_pair = nums[i] + nums[i+1]
                if curr_pair < min_pair:
                    min_pair = curr_pair
                    min_pair_index = i
            
            return min_pair_index

        if is_sorted_ascending(nums):
            return count

        while not is_sorted_ascending(nums):
            index = minPairSum(nums)
            count += 1
            nums[index] +=nums[index+1]
            nums.pop(index+1)
        
        return count



