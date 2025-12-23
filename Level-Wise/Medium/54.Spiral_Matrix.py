class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowBegin = 0
        colBegin = 0
        rowEnd = len(matrix) - 1
        colEnd = len(matrix[0]) - 1
        res = []
        while rowBegin <= rowEnd and colBegin <= colEnd:
            #TraverseRight
            for i in range(colBegin, colEnd+1):
                res.append(matrix[rowBegin][i])
            rowBegin += 1

            #TraverseDown
            for i in range(rowBegin, rowEnd +1):
                res.append(matrix[i][colEnd])
            colEnd -= 1

            #TraverseLeft
            if rowBegin<=rowEnd:
                for i in range(colEnd,colBegin -1, -1):
                    res.append(matrix[rowEnd][i])
            rowEnd -=1

            #TravesrseUp
            if colBegin<=colEnd:
                for i in range(rowEnd,rowBegin -1,-1):
                    res.append(matrix[i][colBegin])
            colBegin += 1



        return res




        