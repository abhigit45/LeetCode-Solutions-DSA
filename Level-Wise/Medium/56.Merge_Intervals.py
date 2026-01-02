class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        output = []
        res = intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0] <= res[-1]:
                res = [min(res[0],intervals[i][0]),max(res[1],intervals[i][1])]
            else:
                output.append(res)
                res = intervals[i]
        output.append(res)
        return output


        
        




            
            
           
   







        