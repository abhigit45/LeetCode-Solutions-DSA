class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = {'T': 0, 'F': 0}  
        max_freq = 0
        max_consecutive = 0
        left = 0
        for right in range(len(answerKey)):
            char = answerKey[right]
            count[char] += 1
            max_freq = max(max_freq, count[char])

            while (right - left + 1) - max_freq > k:
                count[answerKey[left]] -= 1
                left += 1
            max_consecutive = max(max_consecutive, right - left + 1)
        return max_consecutive



        # freq = [0,0]
        # max_consecutive = 0
        # max_freq = 0
        # left = 0
        # for right in range(len(answerKey)):
        #     if answerKey[right] == 'T':
        #         freq[0] += 1
        #     else:
        #         freq[1] += 1
        #     max_freq = max(max_freq,max(freq))

        #     while (right - left + 1) - max_freq > k:
        #         if answerKey[left] == 'T':
        #             freq[0] -= 1
        #         else:
        #             freq[1] -= 1
        #         left += 1
        #     max_consecutive = max(max_consecutive,right - left + 1)
        # return max_consecutive
            




        