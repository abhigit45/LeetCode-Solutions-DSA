class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        freq = {}
        for i in range(len(grid)):
            new_arr = []
            for j in range(len(grid)):
                new_arr.append(grid[j][i])
            key = tuple(new_arr)
            if key in freq:
                freq[key] += 1
            else:
                freq[key] = 1
        for i in grid:
            i_tuple = tuple(i)
            if i_tuple in freq:
                count += freq[i_tuple]
        return count
    
        
        