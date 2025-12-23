class Solution:
    def wiggleSort(self, nums):
        n = len(nums)
        sorted_nums = sorted(nums)
        
        mid = (n + 1) // 2
        left = sorted_nums[:mid][::-1]   
        right = sorted_nums[mid:][::-1]  
        
        for i in range(n):
            if i % 2 == 0:
                nums[i] = left.pop(0)
            else:
                nums[i] = right.pop(0)
