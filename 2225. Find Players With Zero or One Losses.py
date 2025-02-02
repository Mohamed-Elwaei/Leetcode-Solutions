from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        in_degrees = defaultdict(int)

        for winner, loser in matches:
            in_degrees[loser] += 1
            in_degrees[winner] 
        
        ans = [[],[]]
        for player,losses in in_degrees.items():
            if losses == 0:
                ans[0].append(player)
            if losses == 1:
                ans[1].append(player)
        ans[0].sort()
        ans[1].sort()
        return ans