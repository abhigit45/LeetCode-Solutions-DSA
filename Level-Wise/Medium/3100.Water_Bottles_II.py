class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty = 0
        drunk = 0
        while numBottles > 0:
            drunk += numBottles
            empty += numBottles
            numBottles -= numBottles
            
            if empty >= numExchange :
                empty = empty - numExchange
                numExchange += 1
                numBottles += 1
        return drunk


            


            
            
        