"""
Use a union find.
It's best to start with type 3.
Then do type 2 and type 1.

Initially the graph will have n nodes (or components) that are disconnected
First step is to process type 3 edges using a union find.
Then see how many disconnected components are left. If there is one component (the entire graph). Then we are done.

Then we process type 1 and type 2 edges. We return the total no. of edges minus the no. of edges we used of all types.
"""

"""
This function takes in a set of edges, it also takes 2 extra arrays: parent and size.
Parent[u] is the representative of the component u is in.
Size[u] is the size of the component rooted at u.

Union find will return the minimum no. of edges used to make the graph as connected as possible.
It will also modify parent and size.
"""


def union_find(edges, parent, sizes):
    
    def union(u, v):
        u = find(u)
        v = find(v)

        if sizes[v] > sizes[u]:
            u,v = v, u
        
        sizes[u] += sizes[v]
        parent[v] = u
    
    def find(u):
        if u != parent[u]:
            parent[u] = find(parent[u])
        return parent[u]
    
    count = 0

    for u,v in edges:
        if find(u) == find(v): continue
        union(u,v)
        count += 1
    return count



class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        type3 = []
        type2 = []
        type1 = []
        
        V = n
        E = len(edges)

        for type_, u, v in edges:
            u -= 1
            v -= 1
            if type_ == 3:
                type3.append((u,v))
            elif type_ == 2:
                type2.append((u,v))
            elif type_ == 1:
                type1.append((u,v))
        
        parent = [i for i in range(V)]
        sizes = [1] * V

        type3_count = union_find(type3, parent, sizes)

        alice_parent = parent[:]
        alice_sizes = sizes[:]

        bob_parent = parent[:]
        bob_sizes = sizes[:]

        type2_count = union_find(type1, alice_parent, alice_sizes)
        type1_count = union_find(type2,  bob_parent, bob_sizes)

        if max(bob_sizes) < V or max(alice_sizes) < V:
            return -1
        
        return E - (type3_count + type2_count + type1_count)


