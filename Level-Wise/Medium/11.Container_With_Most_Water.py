class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Area=(j−i)×min(height[i],height[j])
        i = 0
        j = len(height)-1
        max_area = 0
        while i < j:
            area = (j-i) * min(height[i],height[j])
            if area > max_area:
                max_area = area
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area
                









        # max_area = 0
        # i = 0
        # j = len(height) - 1
        # while i <  j:
        #     area=(j - i) * min(height[i],height[j])
        #     if area > max_area:
        #         max_area = area
        #     if height [i] < height[j]:
        #         i += 1
        #     else:
        #         j -= 1
        # return max_area
            
        # #BruteForce
        # for i in range(len(height)):
        #     for j in range(i,len(height)):
        #         area=(j-i) * min(height[i],height[j])
        #         if area > max_area:
        #             max_area = area
        # return max_area


