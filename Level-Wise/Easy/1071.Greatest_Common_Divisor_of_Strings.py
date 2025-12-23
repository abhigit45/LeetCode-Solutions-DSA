class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Check concatenation equality
        if str1 + str2 != str2 + str1:
            return ""

        #Find the gcd of the lengths using custom gcd function
        g = gcd(len(str1), len(str2))

        #Candidate substring
        candidate = str1[:g]

        return candidate

        