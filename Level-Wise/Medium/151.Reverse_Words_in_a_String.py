class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1
        
        while i < n:
            if s[i] != ' ':
                word += s[i]
                i += 1
            else:
                # if word != '':
                #     if words != '':
                #         words += " "
                #     words += word
                #     word = ''

                if word != '':
                    words.append(word)
                    word = ''
                while i < n and s[i] == ' ':
                    i += 1
                continue
            
        if word != '':
            words.append(word)
        res = ""
        j = len(words)
        for i in range(-1,-len(words)-1,-1):
            if abs(i)==j:
                res += words[i]
            else:
                res += words[i] + " "

        return res
            

        