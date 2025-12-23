class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_part = version1.split('.')
        v2_part = version2.split('.')

        max_len = 0
        len1 = len(v1_part)
        len2 = len(v2_part)
        if len1 > len2:
            max_len = len1
        else:
            max_len = len2

        for i in range(max_len):
            num1 = 0
            num2 = 0
            if i < len(v1_part):
                num1 = int(v1_part[i])
            else:
                num1 = 0
            if i < len(v2_part):
                num2 = int(v2_part[i])
            else:
                num2 = 0
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        return 0
        


        

        