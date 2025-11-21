class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapp = {'(': ')', '[': ']', '{': '}'}
        
        for char in s:
            if char in mapp:
                stack.append(char)
            else:
                if not stack or mapp[stack[-1]] != char:
                    return False
                stack.pop()
        
        return not stack
