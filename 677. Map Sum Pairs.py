class Node:
    def __init__(self):
        self.children = {c:None for c in 'abcdefghijklmnopqrstuvwxyz'}
        self.end = False
        self.value = 0
class MapSum:

    def __init__(self):
        self.root = Node()
        

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for c in key:
            if curr.children[c] == None:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.end = True
        curr.val = val

    def sum(self, prefix: str) -> int:
        start = self.root
        i = 0
        while start != None and i < len(prefix):
            start = start.children[prefix[i]]
            i += 1
        if start == None : 
            return 0
        total = 0
        def dfs(curr = start):
            nonlocal total
            if curr.end: total += curr.val
            for _,child in curr.children.items():
                if child:
                    dfs(child)
        dfs()
        return total



        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)