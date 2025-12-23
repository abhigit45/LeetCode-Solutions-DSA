class Solution:
    def compress(self, chars: List[str]) -> int:
        ptr = 0
        n = len(chars)
        i = 0 
        
        while i < n:
            count = 1
            while i + 1 < n and chars[i] == chars[i+1]:

                count += 1
                i += 1
            if count > 1:
                if count > 9:
                    chars[ptr] = chars[i]
                    ptr += 1
                    temp = str(count)
                    for j in temp:
                        chars[ptr] = j
                        ptr += 1
                else:

                    chars[ptr] = chars[i]
                    ptr += 1
                    chars[ptr] = str(count)
                    ptr += 1
            else:
                chars[ptr] = chars[i]
                ptr += 1
            i += 1

        return ptr
        