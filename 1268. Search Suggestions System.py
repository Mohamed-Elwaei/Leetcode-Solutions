 
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = {'end':False}
        root = trie

        #Helper Functions
        def add(word): #adds each product to trie
            root = trie
            for l in word:
                if l not in root:
                    root[l] = {'end':False}
                root = root[l]
            root['end'] = True

        #Gives Us <= 3 suggestions for the current query
        def dfs(root, word):
            if root == None or len(tmp) >= 3:
                return
            if root['end'] == True:
                tmp.append(word)

            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c in root:
                    dfs(root[c], word + c)


        for p in products:
            add(p)
        
        suggestions = []
        query = ''
        for l in searchWord:
            if root == None:
                suggestions.append([])
                continue
            root = root.get(l, None)
            query+=l
            tmp = []
            dfs(root,query)
            suggestions.append(tmp[:])
        return suggestions
        