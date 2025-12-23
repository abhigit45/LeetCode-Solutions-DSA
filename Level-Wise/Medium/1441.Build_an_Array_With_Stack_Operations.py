class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stream = 1
        i = 0
        res = []
        stack = []
        while i < len(target) and stream <= n:
            res.append("Push")
            if target[i] == stream:
                i += 1
                # stream += 1
            else:
                res.append("Pop")
            stream += 1
        return res
            

        