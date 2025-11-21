class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        #using stack
        stack = []
        res = ""
        for char in s:
            if char == '(':
                if stack:
                    res += char
                stack.append(char)
            else:  # char == ')'
                stack.pop()
                if stack:
                    res += char
        return res


        # using depth
        depth = 0
        res = ""
        for i in s:
            if i == '(':

                if depth > 0:
                    res += i
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    res += i

        
        return res
