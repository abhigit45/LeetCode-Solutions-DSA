class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        #using binary search optimal

        rows, cols = len(mat), len(mat[0])
        prefix = [[0] * cols for _ in range(rows)]

        # build prefix sum (unchanged)
        for i in range(rows):
            for j in range(cols):
                prefix[i][j] = (
                    (prefix[i-1][j] if i > 0 else 0)
                    + (prefix[i][j-1] if j > 0 else 0)
                    - (prefix[i-1][j-1] if i > 0 and j > 0 else 0)
                    + mat[i][j]
                )

        def sumSquare(r1, c1, r2, c2):
            total = prefix[r2][c2]
            if r1 > 0:
                total -= prefix[r1 - 1][c2]
            if c1 > 0:
                total -= prefix[r2][c1 - 1]
            if r1 > 0 and c1 > 0:
                total += prefix[r1 - 1][c1 - 1]
            return total

        best = 0

        for i in range(rows):
            for j in range(cols):
                lo = best
                hi = min(rows - i, cols - j)

                while lo < hi:
                    mid = (lo + hi + 1) // 2
                    r2 = i + mid - 1
                    c2 = j + mid - 1

                    if sumSquare(i, j, r2, c2) <= threshold:
                        lo = mid
                    else:
                        hi = mid - 1

                best = max(best, lo)

        return best




        # def sumSquare(r1, c1, r2, c2):
        #     total = prefix[r2][c2]

        #     if r1 > 0:
        #         total -= prefix[r1 - 1][c2]
        #     if c1 > 0:
        #         total -= prefix[r2][c1 - 1]
        #     if r1 > 0 and c1 > 0:
        #         total += prefix[r1 - 1][c1 - 1]

        #     return total


        # rows = len(mat) #m
        # cols = len(mat[0]) #n
        # prefix = [[0] * cols for _ in range(rows)]
        # #sum of all element in mat from top_left [0][0] to [i][j]

        # for i in range(rows):
        #     for j in range(cols):
        #         prefix[i][j] = (
        #             (prefix[i-1][j] if i > 0 else 0)
        #             + (prefix[i][j-1] if j > 0 else 0)
        #             - (prefix[i-1][j-1] if i > 0 and j > 0 else 0)
        #             + mat[i][j]
        #         )

        # best = 0 #square maximum size
        # for i in range(rows):
        #     for j in range(cols):
        #         for k in range(min(rows-i,cols-j)): #offset ka for loop
        #             r2 = i + k
        #             c2 = j + k
                
        #             summ = sumSquare(i,j,r2,c2)

        #             if summ <= threshold:
        #                 best = max(best,k+1)
        #             else:
        #                 break
        # return best


