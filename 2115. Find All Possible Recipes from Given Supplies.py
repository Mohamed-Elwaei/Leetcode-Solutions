"""
First thing would be to convert supplies to a set for fast access time.

We can think of this problem as a graph.

Each node u points to v if u is an ingredient of v.

The solution would be using a topological sort. Starting from ingredients

recipes = ["bread","sandwich"], 
ingredients = [["yeast","flour"],["bread","meat"]], 
supplies = ["yeast","flour","meat"]



recipes = ["a","b"], 
ingredients = [["c","b"],["c","a"]], 
supplies = ['c']

Here we would run into a cycle since a needs b and b needs a.
"""

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)

        graph = {x:[] for x in supplies} | {x:[] for x in recipes}
        
        in_degrees = {s:0 for s in supplies}
        
        for i in range(len(recipes)):
            v = recipes[i]
            for u in ingredients[i]:
                graph[u] = graph.get(u, []) + [v]
                in_degrees[v] = in_degrees.get(v,0) + 1
        
    
        level = [x for x in supplies]

        while level:
            nxtLevel = []

            for node in level:
                for neigh in graph[node]:

                    in_degrees[neigh] -= 1
                    if in_degrees[neigh] == 0:
                        nxtLevel.append(neigh)
                    
            level = nxtLevel
        
        answer = []

        for recipe in recipes:
            if in_degrees[recipe] == 0:
                answer.append(recipe)
        return answer

            