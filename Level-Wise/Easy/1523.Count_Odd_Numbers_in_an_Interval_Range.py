class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total = (high - low +1 )// 2
        if low % 2 != 0 and high%2 != 0:
            return total + 1
        else:
            return total
        

        




        #Not optimal
        # count = 0
        # for i in range(low,high +1):
        #     if i % 2 != 0:
        #         count += 1
        # return count
        