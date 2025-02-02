class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        sequences = set()
        N = len(tiles)

        def dfs(num, curr):
            sequences.add(curr)

            for i in range(N):
                if (1 << i) & num: continue
                dfs(num | (1 << i) , curr + tiles[i])
        dfs(0,'')
        return len(sequences) - 1