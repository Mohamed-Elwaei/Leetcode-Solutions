

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = {'end':False}

        def add(folder):
            root = trie
            folder = folder.split('/')
            print(folder)
            for d in folder:
                if d not in root:
                    root[d] = {'end':False}
                root = root[d]
            root['end'] = True

        def removeSubs(folder):
            root = trie
            folder = folder.split('/')
            ret = []
            for d in folder:
                root = root[d]
                ret.append(d)
                if root['end'] == True:
                    break
            return '/'.join(ret)
        for f in folder:
            add(f)
        ans = set()
        for f in folder:
            ans.add(removeSubs(f))
        return ans