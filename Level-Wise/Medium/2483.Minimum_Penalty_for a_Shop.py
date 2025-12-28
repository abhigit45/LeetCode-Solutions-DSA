class Solution:
    def bestClosingTime(self, customers: str) -> int:
        minHour = 0
        penalty = 0
        for i in customers:
            if i == "Y":
                penalty += 1
        minPenalty = penalty
        for i in range(len(customers)):
            if customers[i] == "Y":
                penalty -= 1
            else:
                penalty += 1
            if penalty < minPenalty:
                minPenalty = penalty
                minHour = i+1


        return minHour