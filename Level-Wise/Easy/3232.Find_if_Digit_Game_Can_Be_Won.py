class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        total_single = 0
        total_double = 0
        for num in nums:
            if num < 10:
                total_single += num
            else:
                total_double += num
        if total_single == total_double:
            return False
        else:
            return True

        
        # total = total_single + total_double
        # if total_single > total - total_single:
        #     return True
        # if total_double > total - total_double:
        #     return True
        # return False
        