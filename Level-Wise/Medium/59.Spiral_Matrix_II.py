class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        rowBegin = 0
        rowEnd = len(mat) -1
        colBegin = 0
        colEnd = len(mat[0]) -1
        val = 1
        while rowBegin <= rowEnd and colBegin <= colEnd:
            #Traverse Right
            for i in range(colBegin,colEnd +1):
                mat[rowBegin][i] = val
                val += 1
            rowBegin += 1
            
            #Traverse Down
            for i in range(rowBegin,rowEnd+1):
                mat[i][colEnd] = val
                val +=1
            colEnd -= 1

            #Travsese Left
            if rowBegin <= rowEnd:
                for i in range(colEnd,colBegin - 1,-1):
                    mat[rowEnd][i] = val
                    val += 1
                rowEnd -= 1

            #Travsese UP
            if colBegin <= colEnd:
                for i in range(rowEnd,rowBegin -1,-1):
                    mat[i][colBegin] = val
                    val +=1 
                colBegin += 1
        return mat

        