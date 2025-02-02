class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        ins = [0 for i in range(n)]
        #Check that only one node has 1 indegree (root) and check all other nodes have indegree of 1

        for i in range(len(rightChild)):
            children = [leftChild[i],rightChild[i]]
            for child in children:
                if child!=-1:
                    ins[child] += 1
            
        zeroes = 0
        for degree in ins:
            if degree >=2: #Check if all nodes have in-degree ==1 except root
                return False
            if degree == 0:
                zeroes+=1
        if zeroes !=1: # Check that there's only one root
            return False
        
        visited = set()
        stack = [ins.index(0)] #Start at the root. Where in-degree == 0
        while stack: #DFS search
            curr = stack.pop()
            visited.add(curr)

            for child in [leftChild[curr],rightChild[curr]]:
                if child==-1:
                    continue
                if child in visited: #Check for cycles
                    return False
                else:
                    stack.append(child)
          
        return len(visited) == n #Check that the tree is connected
            
        