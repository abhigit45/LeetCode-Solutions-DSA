class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
        MOD = 10**9 + 7

        # Add boundary fences
        hFences.insert(0, 1)
        hFences.append(m)
        vFences.insert(0, 1)
        vFences.append(n)

        # Sort fences
        hFences.sort()
        vFences.sort()

        heights = set()
        widths = set()

        # All possible horizontal distances
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                heights.add(hFences[j] - hFences[i])

        # All possible vertical distances
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                widths.add(vFences[j] - vFences[i])

        # Find maximum possible square side
        max_side = 0
        for d in heights:
            if d in widths:
                max_side = max(max_side, d)

        if max_side == 0:
            return -1

        return (max_side * max_side) % MOD
