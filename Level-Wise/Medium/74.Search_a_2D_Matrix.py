class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Binary Serch
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = m*n-1

        while left <= right:
            mid = left + (right - left)//2

            row = mid//n
            col = mid%n
            if matrix[row][col] > target:
                right = mid - 1
            elif matrix[row][col] < target:
                left = mid +1 
            else:
                return True
        return False
            





        # i = 0
        # j = len(matrix[0]) - 1
        # while i < len(matrix) and j >= 0 :
        #     if matrix[i][j] < target:
        #         i += 1
        #     elif matrix[i][j] > target:
        #         j -= 1
        #     else:
        #         return True
        # return False



        