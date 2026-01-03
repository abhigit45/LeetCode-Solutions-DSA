class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        n = len(nums)
        low = 0
        high = n-1
        while low < high:
            mid = (low+high)//2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]
            
        





        # # bruteForce
        # n = len(nums)
        # minn = float('inf')
        # for x in range(n):
        #     rotated_arr = nums[x:] + nums[:x]
        #     if rotated_arr[0] < minn:
        #         minn = rotated_arr[0]
        # return minn



        # funny soln
        # return min(nums)
        