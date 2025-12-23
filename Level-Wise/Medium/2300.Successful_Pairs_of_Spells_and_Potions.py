class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        output = [0] * len(spells)
        potions.sort()

        for i in range(len(spells)):
            left = 0
            right = len(potions) - 1
            while left <= right:
                mid = (left + right) // 2
                product = potions[mid] * spells[i]
                if product >= success:
                    right = mid - 1
                else:
                    left = mid +1
            output[i] = len(potions) - left
        return output



        
        # output = []
        # for i in range(len(spells)):
        #     res = []
        #     for j in range(len(potions)):
        #         res.append(spells[i] *potions[j])
        #     count = 0
        #     for k in res:
        #         if k >= success:
        #             count += 1
        #     output.append(count)
        # return output

