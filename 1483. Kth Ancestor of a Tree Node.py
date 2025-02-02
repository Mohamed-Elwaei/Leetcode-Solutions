
class TreeAncestor:
    steps = 15
    def __init__(self, n: int, parent: list[int]):
        currLvl = {index:parent for index,parent in enumerate(parent)}
        dp = [currLvl]
        for _ in range(self.steps):
            nextLvl = {}
            for node in currLvl:
                parent = currLvl[node]
                if parent in currLvl:
                    nextLvl[node] = currLvl[parent]
            dp.append(nextLvl)
            currLvl = nextLvl
        self.dp = dp

    def getKthAncestor(self, node: int, k: int) -> int:
        dp = self.dp
        step = self.steps
        while k > 0 and node > -1:
            if 1 << step <= k:
                node = dp[step].get(node,-1)
                k -= 1 << step
            else:
                step -= 1
        return node
    