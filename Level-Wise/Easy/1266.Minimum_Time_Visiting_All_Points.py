class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        step = 0
        for i in range(0,n-1):
            x1 = points[i][0]
            y1 = points[i][1]

            x2 = points[i+1][0]
            y2 = points[i+1][1]

            dy = abs(y2-y1)
            dx = abs(x2-x1)

            step += (min(dy,dx) + abs(dy-dx))
        return step

        