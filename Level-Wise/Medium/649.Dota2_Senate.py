class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad = []
        dire = []
        n = len(senate)
        for i in range(n):
            if senate[i] == "R":
                rad.append(i)
            else:
                dire.append(i)
     
        while rad and dire:
            r = rad.pop(0)
            d = dire.pop(0)
            if r > d:
                dire.append(d+n)
               
            else:
                rad.append(r+n)
           
        if dire:
            return "Dire"
        else:
            return "Radiant"

        