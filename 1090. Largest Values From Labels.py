from collections import defaultdict
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        #values = [5,4,3,2,1], labels = [1,3,3,3,2]. Picked: 
        #We pick 5 with label 1. Picked: 1:1
        #We pick 4 with label 3. Picked 1:1, 3:1
        #We pick 3 with label 3. Picked 1:1 3:2

        items = [item for item in zip(values,labels)] #O(n) in time and Memory
        items.sort(key = lambda item: -item[0]) # sort items by descending values and store their labels

        inventory = defaultdict(int) #Map each item's label to how many of that label we have.
        score = 0
        for value, label in items:
            if inventory[label] >= useLimit: continue
            #Check if we can pick the item. Make sure we don't go over the useLimit
            inventory[label] += 1
            score += value
            numWanted -= 1

            if numWanted == 0: # Early exit
                return score
        return score

        #Memory Complexity O(n) due to inventory and items variables.
        #Time complexity is O(n log(n)) due to sorting.
        

        