class Solution:
    def cal(self,a,b,token):
        if token == "+":
            return b+a
        if token == "-":
            return b-a
        if token == "*":
            return b*a
        if token == "/":
            return int(b/a)
        return -1
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                # a = int(stack[-1]) 
                a = int(stack.pop()) 
                # b = int(stack[-2])
                b = int(stack.pop())
                res = self.cal(a,b,token)
                stack.append(res)
            else:
                stack.append(int(token))
        
        return stack[-1]

        