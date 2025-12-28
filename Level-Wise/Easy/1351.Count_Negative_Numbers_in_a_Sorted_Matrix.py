class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0
        for i in range(len(grid)):
            neg_idx = len(grid[i])
            left = 0
            right = len(grid[i]) - 1
            while left <= right:
                mid = int(left + (right - left)/2)
                if grid[i][mid] < 0:
                    neg_idx = mid
                    right = mid - 1
                else:
                    left = mid+1
           
            count += len(grid[i]) - neg_idx
        return count
            
            
                



        # count = 0
        # for i in range(len(grid[0])):
        #     for j in range(len(grid)):
        #         if grid[j][i] < 0:
        #             count += 1
        # return count
        