class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:   
                res[i] = stack[-1] - i
    
            stack.append(i)
        return res







        # #bruteForce
        # res= [0] * len(temperatures)
        # for i in range(len(temperatures)):
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j-i
        #             break
        # return res



        