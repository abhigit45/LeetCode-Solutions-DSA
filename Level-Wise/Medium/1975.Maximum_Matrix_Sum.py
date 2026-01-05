class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg_count = 0
        smallest_number = float('inf')
        total = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                num = matrix[i][j]
                if num < 0:
                    neg_count += 1
                total += abs(num)
                if smallest_number > abs(num):
                    smallest_number = abs(num)
                
        if neg_count %2 == 1:
            total -= 2*smallest_number
        return total
            

        