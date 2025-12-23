class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = 0
        empty = 0
        while numBottles > 0:
            if numBottles > 0:
                numBottles -= 1
                empty += 1
                total += 1
            if empty == numExchange:
                numBottles += empty//numExchange
                empty -= numExchange
        return total

        #Optimized
        # while numBottles > 0:
        #     total += numBottles
        #     empty += numBottles
        #     numBottles = empty // numExchange
        #     empty = empty % numExchange




        