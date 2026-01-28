class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        m = len(players)
        n = len(trainers)
        i = 0
        j = 0
        count = 0
        while i < m and j < n:
            if players[i] <= trainers[j]:
                count += 1
                i += 1
                j += 1
            else:
                j+=1
        return count
                

        