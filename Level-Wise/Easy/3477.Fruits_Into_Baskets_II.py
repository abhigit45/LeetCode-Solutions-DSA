class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0
        for fruit in fruits:
            for i in range(len(baskets)):
                if fruit <= baskets[i]:
                    baskets[i] = 0
                    count += 1
                    break

        return len(fruits) - count
            


        