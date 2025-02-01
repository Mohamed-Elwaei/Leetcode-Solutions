class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        n = len(people)
        people.sort()

        ret = [None] * n

        #We place person i with height i, and order i in the first empty slot where there are order people with greater than
        # or equal heights or empty slots.
        for height, order in people:
            tmp = 0
            for slot in range(n):
                if tmp >= order and ret[slot] == None:
                    ret[slot] = [height,order]
                    break
                elif ret[slot] == None or ret[slot][0] >= height:
                    tmp += 1
        
        return ret
