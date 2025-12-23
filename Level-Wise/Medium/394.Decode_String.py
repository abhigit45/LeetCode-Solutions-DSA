class Solution:
    def decodeString(self, s: str) -> str:
        numStack = []
        stringStack = []
        num = ""
        for i in range(len(s)):
            if s[i].isdigit():
                num += s[i]
            elif s[i] != "]":
                if num != "":
                    numStack.append(int(num))
                    num = ""
                stringStack.append(s[i])
            else:
                strr = ''
                
                while stringStack[-1] != '[':
                    strr = stringStack.pop() + strr
                stringStack.pop()
                numm = numStack.pop()
                addd = numm * strr

                stringStack.append(addd)
        return "".join(stringStack)

                
                



        


        