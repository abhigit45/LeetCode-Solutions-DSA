class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # -4,-1,1,2
        sorted_array = sorted(nums)
        n = len(sorted_array)
        res = float('inf')
        closet = float('inf')
        for i in range(n-2):
            left = i + 1
            right = n - 1
            while left < right:
                total = sorted_array[i] + sorted_array[left]+ sorted_array[right]
                diff = abs(total - target) 
                if diff < closet:
                    closet = diff
                    res = total
                
                if total < target:
                    left += 1
                else:
                    right -= 1
        return res
                
                